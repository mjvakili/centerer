The revised manuscript achieves the authors' stated goal of focusing on the comparison of known centroiding methods, rather than the previous manuscript's implied goal of proposing a centroiding method that has been in the literature for decades (although not widely used). I greatly appreciate the significant rewrite to this effect.

Additionally, the authors have also made more explicit their assumptions of stationary Gaussian noise, and the conditions in astronomical imaging where this may be expected. Finally, I appreciate the updates throughout to respond to my previous minor comments.

While I appreciate the revised paper's focus on centroid accuracy, I must note that the analytical form of maximum likelihood (as a function of the star's position) is a simple function of the matched filter output divided by sqrt(dot(m,m)) using the nomenclature of Equation 30. So, it is self-evident that the two methods should perform equivalently for all but small PSFs (where dot(m,m) cannot be assumed to be constant). As such, I do not believe that article meets the scientific criteria of the AJ and do not recommend its publication.


I do believe there is potential for an interesting and useful paper if the authors would address conditions more representative of what most astronomers face, where the matched-filter and maximum-likelihood forms are not so trivially related to each other. Several examples follow that specifically address how well a matched-filter algorithm compares with more sophisticated (but much slower) PSF-fitting routines:

1. How well would the matched filter compare with the CRLB if the noise model is dominated by Poisson noise from the star instead of by constant noise from the sky?

2. How do neighbor stars impact the quality of the matched-filter centroid, relative to a PSF-fitting solution that solves for both stars' positions?

3. For stars in nebulae or resolved nearby galaxies, how much of a gradient in the "background subtracted" frame can be tolerated without significant degradation of the centroid (compared with a PSF-fitting solution that accounts for gradients)?

Another interesting question, given the amount of space telescope data taken with undersampled PSFs: do Figures 5-8 show significant deterioration if they were extended to 1 pixel FWHM?


Minor comments:

- Section 2, paragraph 4 (beginning "A number of"): two of the most frequent causes of correlated pixel noise are the widespread use of CTE-corrected images and drizzling.

- Section 2, paragraph 16 (beginning "The optimal"): The optimal estimator of flux is sum_i(y_i*P_i) / sum_i(P_i^2). Thus, it is proportional to the matched-filter estimator, not equal to the matched-filter estimator (assuming the denominator is constant).

- Section 5.1, paragraph 3. I believe that the the reason for the excellent match to the 2.8 pixel FWHM case is that the smoothing filter is nearly the same as the PSF, not because of fractional information within a 3x3 patch of the image.

- Section 6. I would still like to see a comparison of execution time for a PSF fitting algorithm vs. a matched filter algorithm. I believe that the key take-away from this paper is that the matched filter algorithm produces centroids that are nearly as accurate as those from a maximum likelihood approach in a fraction of the computational time. A comparison will give the reader a benchmark to understand whether or not the slight improvement (from PSF fitting) is worth the resources required.
