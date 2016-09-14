from __future__ import absolute_import
from .histogram_base import HistogramBase
from .histogram_nd import HistogramND
from .histogram1d import Histogram1D
from . import binnings, histogram_nd
import numpy as np
import math
from functools import reduce


class TransformedHistogramMixin(object):
    """Histogram with non-cartesian (or otherwise transformed) axes.

    This is a mixin, providing transform-aware find_bin, fill and fill_n.

    When implementing, you are required to provide tbe following:
    - `transform` method to convert rectangular (suggested to make it classmethod)
    - `bin_sizes` property

    In certain cases, you may want to have default axis names + projections.
    Look at PolarHistogram / SphericalHistogram / CylindricalHistogram as
    an example.
    """

    @classmethod
    def transform(self, value):
        """Convert cartesian coordinates into internal ones.

        Parameters
        ----------
        value : array_like
            This method should accept both scalars and numpy arrays.
            If multiple values are to be transformed, it should of
            (nvalues, ndim) shape.

        Returns
        -------
        float or array_like
        """
        raise NotImplementedError("TransformedHistogramMixin descendant must implement transform method.")

    def find_bin(self, value, axis=None, transformed=False):
        """

        Parameters
        ----------
        value : array_like
            Value with dimensionality equal to histogram.
        transformed : bool
            If true, the value is already transformed and has same axes as the bins.
        """
        if axis is None and not transformed:
            value = self.transform(value)
        return HistogramND.find_bin(self, value, axis=axis)

    @property
    def bin_sizes(self):
        raise NotImplementedError("TransformedHistogramMixin descendant must implement bin_sizes property.")

    def fill(self, value, weight=1, transformed=False):
        return HistogramND.fill(self, value=value, weight=weight, transformed=transformed)

    def fill_n(self, values, weights=None, dropna=True, transformed=False):
        if not transformed:
            values = self.transform(values)
        HistogramND.fill_n(self, values=values, weights=weights, dropna=dropna)


class PolarHistogram(TransformedHistogramMixin, HistogramND):
    """2D histogram in polar coordinates.

    This is a special case of a 2D histogram with transformed coordinates:
    - r as radius in the (0, +inf) range
    - phi as azimuthal angle in the (0, 2*pi) range

    """
    def __init__(self, binnings, frequencies=None, **kwargs):
        if not "axis_names" in kwargs:
            kwargs["axis_names"] = ("r", "phi")
        if "dim" in kwargs:
            kwargs.pop("dim")
        super(PolarHistogram, self).__init__(2, binnings=binnings, frequencies=frequencies, **kwargs)

    @property
    def bin_sizes(self):
        sizes = 0.5 * (self.get_bin_right_edges(0) ** 2 - self.get_bin_left_edges(0) ** 2)
        sizes = np.outer(sizes, self.get_bin_widths(1))
        return sizes

    @classmethod
    def transform(self, value):
        value = np.asarray(value, dtype=np.float64)
        assert value.shape[-1] == 2
        result = np.empty_like(value)
        result[...,0] = np.hypot(value[...,1], value[...,0])
        result[...,1] = np.arctan2(value[...,1], value[...,0]) % (2 * np.pi)
        return result

    def projection(self, axis_name, **kwargs):
        if isinstance(axis_name, int):
            ax = axis_name
        elif axis_name == self.axis_names[0]:
            ax = 0
        elif axis_name == self.axis_names[1]:
            ax = 1
        else:
            raise RuntimeError("Unknown axis: {0}".format(axis_name))
        klass = (RadialHistogram, AzimuthalHistogram)[ax]
        return HistogramND.projection(self, ax, type=klass, **kwargs)

    # TODO: fill_n() does not work


class RadialHistogram(Histogram1D):
    """Projection of polar histogram to 1D with respect to radius.

    This is a special case of a 1D histogram with transformed coordinates.
    """
    @property
    def bin_sizes(self):
        return (self.bin_right_edges ** 2 - self.bin_left_edges ** 2) * np.pi

    def fill_n(self, values, weights=None, dropna=True):
        # TODO: Implement?
        raise NotImplementedError("Radial histogram is not (yet) modifiable")

    def fill(self, value, weight=1):
        # TODO: Implement?
        raise NotImplementedError("Radial histogram is not (yet) modifiable")


class AzimuthalHistogram(Histogram1D):
    """Projection of polar histogram to 1D with respect to phi.

    This is a special case of a 1D histogram with transformed coordinates.
    """
    # TODO: What about fill(_n)? Should it be 1D or 2D?
    # TODO: Add special plotting (polar bar, polar ring)
    def fill_n(self, values, weights=None, dropna=True):
        raise NotImplementedError("Azimuthal histogram is not (yet) modifiable")

    def fill(self, value, weight=1):
        raise NotImplementedError("Azimuthal histogram is not (yet) modifiable")


class SphericalHistogram(TransformedHistogramMixin, HistogramND):
    """3D histogram in spherical coordinates.

    This is a special case of a 2D histogram with transformed coordinates:
    - r as radius in the (0, +inf) range
    - theta as angle between z axis and the vector, in the (0, 2*pi) range
    - phi as azimuthal angle  (in the xy projection) in the (0, 2*pi) range
    """

    def __init__(self, binnings, frequencies=None, **kwargs):
        if not "axis_names" in kwargs:
            kwargs["axis_names"] = ("r", "theta", "phi")
        kwargs.pop("dim", False)
        super(SphericalHistogram, self).__init__(3, binnings=binnings, frequencies=frequencies, **kwargs)

    @classmethod
    def transform(self, value):
        value = np.asarray(value, dtype=np.float64)
        result = np.empty_like(value)
        x, y, z = value.T
        xy = np.hypot(x, y)
        result[...,0] = np.hypot(xy, z)
        result[...,1] = np.arctan2(xy, z) % (2 * np.pi)
        result[...,2] = np.arctan2(y, x) % (2 * np.pi)
        return result

    @property
    def bin_sizes(self):
        sizes1 = (self.get_bin_right_edges(0) ** 3 - self.get_bin_left_edges(0) ** 3) / 3
        sizes2 = np.cos(self.get_bin_left_edges(1)) - np.cos(self.get_bin_right_edges(1))
        sizes3 = self.get_bin_widths(2)
         # Hopefully correct
        return reduce(np.multiply, np.ix_(sizes1, sizes2,sizes3))
        #return np.outer(sizes, sizes2, self.get_bin_widths(2))    # Correct


class CylindricalHistogram(TransformedHistogramMixin, HistogramND):
    """3D histogram in cylindrical coordinates.

    This is a special case of a 2D histogram with transformed coordinates:
    - r as radius projection to xy plane in the (0, +inf) range
    - phi as azimuthal angle  (in the xy projection) in the (0, 2*pi) range
    - z as the last direction without modification, in (-inf, +inf) range
    """
    def __init__(self, binnings, frequencies=None, **kwargs):
        if not "axis_names" in kwargs:
            kwargs["axis_names"] = ("rho", "phi", "z")
        kwargs.pop("dim", False)
        super(CylindricalHistogram, self).__init__(3, binnings=binnings,
              frequencies=frequencies, **kwargs)

    @classmethod
    def transform(self, value):
        value = np.asarray(value, dtype=np.float64)
        result = np.empty_like(value)
        x, y, z = value.T
        result[...,0] = np.hypot(x, y)                     # tho
        result[...,1] = np.arctan2(y, x) % (2 * np.pi)     # phi
        result[...,2] = z
        return result

    @property
    def bin_sizes(self):
        sizes1 = 0.5 * (self.get_bin_right_edges(0) ** 2 - self.get_bin_left_edges(0) ** 2)
        sizes2 = self.get_bin_widths(1)
        sizes3 = self.get_bin_widths(2)
        return reduce(np.multiply, np.ix_(sizes1, sizes2, sizes3))


def _prepare_data(data, transformed, klass,  *args, **kwargs):
    data = np.asarray(data)
    if not transformed:
        data = klass.transform(data)
    dropna = kwargs.get("dropna", False)
    if dropna:
        data = data[~np.isnan(data).any(axis=1)]
    return data


def polar_histogram(xdata, ydata, radial_bins="human", phi_bins=16, transformed=False, *args, **kwargs):
    """

    Parameters
    ----------
    transformed : bool
    phi_range : Optional[tuple]
    range
    """
    dropna = kwargs.pop("dropna", True)
    data = np.concatenate([xdata[:, np.newaxis], ydata[:, np.newaxis]], axis=1)
    print(data)
    data = _prepare_data(data, transformed=transformed, klass=PolarHistogram, dropna=dropna)
    print(data)
    # print(data.shape)

    if isinstance(phi_bins, int):
        phi_range = (0, 2 * np.pi)
        if "phi_range" in "kwargs":
            phi_range = kwargs["phi_range"]
        elif "range" in "kwargs":
            phi_range = kwargs["range"][1]
        phi_range = list(phi_range) + [phi_bins + 1]
        phi_bins = np.linspace(*phi_range)

    bin_schemas = binnings.calculate_bins_nd(data, [radial_bins, phi_bins], *args, check_nan=not dropna, **kwargs)
    weights = kwargs.pop("weights", None)
    frequencies, errors2, missed = histogram_nd.calculate_frequencies(data, ndim=2,
                                                                  binnings=bin_schemas,
                                                                  weights=weights)
    return PolarHistogram(binnings=bin_schemas, frequencies=frequencies, errors2=errors2, missed=missed)


def spherical_histogram(data=None, radial_bins="human", theta_bins=16, phi_bins=16, transformed=False, *args, **kwargs):
    dropna = kwargs.pop("dropna", True)
    data = _prepare_data(data, transformed=transformed, klass=SphericalHistogram, dropna=dropna)

    # TODO: Add arguments to construct bins

    bin_schemas = binnings.calculate_bins_nd(data, [radial_bins, theta_bins, phi_bins], *args,
                                             check_nan=not dropna, **kwargs)
    weights = kwargs.pop("weights", None)
    frequencies, errors2, missed = histogram_nd.calculate_frequencies(data, ndim=3,
                                                                  binnings=bin_schemas,
                                                                  weights=weights)
    return SphericalHistogram(binnings=bin_schemas, frequencies=frequencies, errors2=errors2, missed=missed)
