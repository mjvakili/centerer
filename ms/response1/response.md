Dear Editor,

This was a very helpful and constructive referee report and we have revised the paper
accordingly. We think the referee comments have improved the paper
substantially.

Mohammadjavad Vakili (on behalf of the authors)

-----

We very much appreciate the thorough and constructive referee comments;
they have led to substantial improvements in the paper. 
In what follows, the referee comments are indented and our responses are not
indented.


  Referee comment: 

  The authors propose the use of matched filtering to centroid bright stars as an alternative to more computationally expensive PSF-fitting algorithms. 
  The manuscript contains a handful of tests demonstrating that matched    filtering is as accurate as PSF-fitting in most regimes of SNR and PSF size.
  My primary concern is that matched filtering is an accepted technique that has been in the literature for decades (e.g., Ribak, Hege & Christou 1985) and
  predates the use of PSF-fitting. This study proposes using a quadratic interpolator to estimate the peak of a matched filter, 
  which I do not believe meets the Astronomical Journal's criteria for significant contribution to the  literature.

Our response: 

We want to point out that the aim of our investigation is not introducing a new method for estimating the centroids of stars. As the referee has pointed out, the matched-filter polynomial centroiding method has been widely used in the astronomy literature. We do not wish to present a novel method for centroiding stars. Our goal for writing this manuscript is to show whether or not fast and approximate methods can saturate the fundamental Cram\'{e}r-Rao lower bound on the centroiding errors. We apologize to the referee if we failed to make it clear that the scope of our investigation is limited to testing the saturation of the Cram\'{e}r-Rao lower bound on centroiding errors. 
We have made major changes to the abstract and the introduction of our manuscript.  We have broken the first paragraph of the abstract to two paragraphs. we begin the second paragraph by explaining the CRLB. Afterwards, we aim to compare the performance of various centroiding methods, in terms of saturating the bound. We omit the paragraph in the intro that discussed software packages for astrometry and photometry of stars. We mostly focus on discussions related to CRLB.     

  Referee comment: 

  First, astronomical images do not have stationary noise. Additionally, for cameras with low background levels, 
  the Gaussian noise assumption is invalid as the photon noise distribution becomes asymmetric at low flux levels and 
  noise is quantized into counts during readout. While I understand that the limitations of the authors'  analysis 
  require stationary Gaussian noise, one suspects that the interdependence of brightness and noise (and thus  centroid) 
  may adversely impact the technique advocated in this paper.
  For example, equations 13-17 in section 2 are only valid for constant pixel noise, while an astronomical image containing 
  sources not only has variable noise but the noise itself is a function of the brightness of the sources.   The reader is thus left to suspect that use of a realistic noise model could alter the outcomes of the tests presented.

Our response:

We agree with the referee's comment that the the assumption of stationary noise is not in general true. However, we make it clear in the introduction that we limit the scope of our paper to the sky-limited images for which sky level has been subtracted and any instrument gain has been calibrated out. 
In the introduction section, we added two paragraphs that briefly explain the underlying assumptions of our data generation procedure. In the 5th paragraph of the introduction, we briefly overview the various sources of noise that could potentially cause deviation of centroiding errors from the CRLB. We also explicitly mention that we limit our investigation to the simulated images that are sky limited. 
In the 6th paragraph of introduction, we we discuss the general assumptions we make in our investigation. These assumptions include perfect flat-field calibration, lack of contamination by cosmic rays, etc. 

Furthermore, in section 2 of the manuscript, we provide explanation for the assumption of stationary noise process listed in the assumptions in the bullet points. After the bullet points, we have added two paragraphs in order to explain these assumptions. We mention in the text that we explicitly focus on sky-limited images, for which the Poisson noise is mostly dominated by the sky.  We also mention 
that in the limit where the number of photons per pixel is large, the Poisson noise can be approximated by a Gaussian distribution. This is a very good approximation for many astronomical imaging datasets such as the Sloan Digital Sky Survey, DECAM Legacy Survey,  etc. 

  Referee comment:

  A second major concern is that the authors have not discussed the potential impact of sampling PSFs in the center of each pixel vs. 
  integrating the PSF over a pixel.  While this has minimal impact on Nyquist-sampled images, undersampled images such as those from WFC3/IR suffer from 
  significant variation of the PSF within a pixel, which can create errors in  the inferred centroiding (e.g., Anderson & King 2000). 
  While the authors do not indicate whether they sample or integrate, this is a key concern for   any discussion of centroiding and must be included in this paper.

Our response:

The model of the PSF considered in our manuscript is a model of  the pixel-convolved PSF which is the instrumental PSF convolved with the pixel response function. 
It is the pixel-convolved PSF that can be directly estimated from observations without making any assumption about the sensitivity of detector pixels. Moreover, it is the pixel-convolved PSF that can be used to perform astrometry and photometry measurements as well as galaxy shape measurements in weak lensing.

In the third page of our manuscript we have added a paragraph explaining the assumptions about the PSF model used in  our data generation. First, we mention that the simulated images (in the pixel space) are close to Nyquist-sampled or close to 
Nyquist-sampled. Then, we mention that the pixels in the simulated images are identical and the stars are simulated by sampling from the pixel-convolved PSF. This concept is thoroughly explained in (Anderson & King 2000). Note that in that paper, the pixel-convolved PSF is referred to as the effective PSF. 

We are aware of the challenges that one might in modeling astronomical images for which the PSF is under-sampled such as the images observed by the HST WFC3-IR channel. In such cases, the solution for the super-resolution (super-sampled) pixel-convolved PSF is degenerate with the centroid offsets of stars. Therefore, estimating the super-resolution PSF in those images requires imposing extra conditions for breaking those degeneracies. In a nearly-completed manuscript (Vakili, Hogg, and Fadely in prep) we are presenting a data-driven model for estimating the super-resolution PSF from under-sampled images of the HST WFC3-IR channel. In this manuscript, we specifically focus on the Nyquist-sampled or close to Nyquist-sampled images. We agree with the referee comment and we have clarified the assumptions we made for simulating the images in our manuscript. 


We agree with the referee's comment that the RMSE approaches the CRLB and we replaced the expression "becomes greater than or equal to approaches

  Referee comment:

  A third concern about the analysis is that the impact of neighboring sources is never discussed. 
  A specific concern about the matched filter is that smoothing the image wipes out any fainter neighbors, while PSF-fitting 
  photometry approaches are able to accurately obtain astrometry and photometry of sources separated by  the image FWHM.

Our response:

The purpose of this manuscript is to investigate whether fast stellar centroiding methods can saturate the Cramer-Rao lower bound or not when they are applied to single isolated stars. 
The PSF-fitting method based that delivers a maximum-likelihood estimator of the centroid of a given star can saturate this fundamental theoretical bound as long as a correct model 
of the PSF is used.  In analysis of the data from the wide imaging surveys such as the Sloan Digital Sky Survey and the upcoming Large Synoptic Survey Telescope (LSST), fast approximate methods 
are used to estimate the centroids of stars. One of these methods is the well-known matched-filter polynomial centroiding estimator that we include in our study. We only wish to investigate whether these 
fast estimators are able to saturate the Cramer-lower bound on stellar centroiding errors or not.  For investigating the saturation of the Cramer-Rao lower bound, it is sufficient to see whether these methods 
are capable of saturate the bound when applied to images of isolated stars or not. 

  Referee comment:

  - Section 1, paragraph 1: it is unclear why the PSF would be "wrongly estimated", unless the centroid is calculated incorrectly.

Our response:

We just wanted to point out that in a forward model of the image of a given star, it is the PSF model 
that should be shifted to the center of the star. The image of the star itself should not be shifted.
But we note that it is not necessary to include this and it is not related to the goal of this paper. 
So we dropped that sentence from the manuscript.

  Referee comment:

  - Section 1, paragraph 4: there are significantly more noise sources than sky and CCD readout noise: photon noise from the object, flatfield errors, bias/overscan subtraction errors, etc.

Our response:

We agree with the referee comment. In paragraph of 5 of section 1 we have included many more examples of possible noise sources such as the CCD readout noise, sky noise, errors resulting from 
incorrect flat-field calibration, and photon noise from the astronomical object itself. We end this paragraph by mentioning that we limit the focus of our investigation to 
the simulated images with non-overlapping faint sources that are sky limited. In paragraph 6 of section 1, we list other assumptions we have made for simulating images. 
Furthermore, we assume that the sky has been subtracted, instrument gain has been calibrated out, and that the simulated images are free of contamination by cosmic rays, 
stray light from neighboring fields, and any other defect.

  Referee comment: 

  - Section 2, paragraph 3, bullet 2: "noise" is misspelled

Our response:

We corrected that.

  Referee comment:

  - Section 2, paragraph 10 (beginning with "Asymptotically"): since the RMS is always "greater than or equal to the CRLB", I believe the authors mean that the RMS "approaches the CRLB".

Our response:

We agree with the author. We changed this to "approaches the CRLB".

  Referee comment: 

  Given that the authors are using simulated data, a direct search for biases in the estimator outputs is far more powerful than using violations of the Cramer-Rao inequality to infer biased techniques.

Our response: 

we are sorry if this sentence implies that we are using the CRLB to estimate biases. 
We do not wish to use use CRLB as a proxy to determine the biases arising from centroiding methods. 
This is not the purpose of this investigation. We notice that the entire discussion of beating the CRLB may 
imply that we want to see whether we can find biases by looking at whether 
the CRLB is beaten or not. We realized that this does not serve any purpose in our investigation. 
We drop the paragraph starting with "However, the relation (3) does not necessarily hold for biased estimators..." 
and the entire discussion of "beating the CRLB". We apologize if that have caused any confusion. 


  Referee comment:

  As a point of formatting, the manuscript could benefit from use of subsections. For example, section 3 is four pages long in the version provided, 
  with four major subsections highlighted by bold text. I suggest the authors make these sections 3.1, 3.2, 3.3, and 3.4.

Our response:

We agree with this comment. We have divided section 3 to four subsection: 3.1, 3.2, 3.3, and 3.4.

  Referee comment:

  the authors imply the PSF-fitting can only be used when the PSF is known. This is not true; one of the variables in PSF-fitting algorithms is often the PSF size (and sometimes shape) itself.

Our response:

We apologize the referee if has caused any confusion. We have this clarified this in subsection 3.4. 
We mention that the PSF-fitting method in our investigation is done by maximizing a likelihood functions which assumes a correct model 
of the PSF (Moffat profile) with  a correct size. Given that the correct PSF is assumed, we expect the RMSE arising from this method 
to saturate the CRLB. Therefore, this method serves as the most efficient estimator, in that it preserves the most amount of information (encoded in the 
Fisher information matrix) that can be achieved in the presence of noise. 
  
  Referee comment:
  
  - Section 3, "Default polynomial centroiding" section. The use of a 7x7 kernel appears arbitrary. For the sake of a fair comparison with the matched filter, 
  the size of the kernel should be equivalent to that used in the   matched filter section.

Our response:

We completely agree with the referee that the use of a 7x7 kernel seems arbitrary. In order to present a fair comparison between this method 
and the matched filter method, we use the same kernel size that is used in the matched-filter method. Furthermore, we found that the title 
"Default polynomial centroiding" is ambiguous. Thus, we changed that to "Fixed-Gaussian polynomial centroiding". This names refers to 
the fact that a Gaussian kernel with a fixed size is applied in this method. 

  Referee comment:

  - Section 6, paragraph 2: The authors imply the PSF-fitting can only be used when the PSF is known. This is not true; one of the variables in PSF-fitting algorithms is often the PSF size (and sometimes shape) itself.

Our response:

We apologize the referee if has caused any confusion. We have this clarified this in subsection 3.4. 
We mention that the PSF-fitting method in our investigation is done by maximizing a likelihood functions which assumes a correct model 
of the PSF (Moffat profile) with  a correct size. Given that the correct PSF is assumed, we expect the RMSE arising from this method 
to saturate the CRLB. Therefore, this method serves as the most efficient estimator, in that it preserves the most amount of information (encoded in the 
Fisher information matrix) that can be achieved in the presence of noise. 

  Referee comment:

  - Section 6, paragraph 3: The authors should quantify the difference in accuracy between the 7x7 moment method and an optimal estimator. Is it 10% worse? 10x worse?

Our response:

We agree with this and we have included some numbers in order to quantify the difference. We mention the difference in 
terms of the ratio between the root-mean-squared error and the CRLB. For an optimal estimator, 
the ratio is one or very close to one. This discussion is now moved to paragraph 5 of section 6. In paragraph 5 of section 6, 
we quantify the percentage deviation of the 7x7 moment centroiding errors from the CRLB.

  Referee comment:

  - Section 6, paragraph 4: The intent of the statement that the default polynomial centroiding uses only a 3x3 pixel region of the smoothed image is unclear. 
  While this is a factually true statement, the smoothing algorithm   requires far more than 3x3 pixels on the original image to operate.

Our response:


In the new version of the manuscript, this paragraph has been moved to section 6, paragraph 6. 
We agree with the referee that smoothing algorithm requires information far more than the 3x3 pixels 
on the original image. We dropped that sentence that claims the fixed Gaussian polynomial centroiding 
(previously noted as default Gaussian centroiding) only uses information in the 3x3 region. 
Furthermore, we drop all the sentences that discuss the effect of smoothing on sampling. 

  Referee comment:

  - Section 6, paragraph 6: If PSF-fitting is to be argued against for speed reasons, the authors should compare the speed of PSF-fitting 
  astrometry and flux estimates against matched filter astrometry plus PSF-fitting flux   estimation. It is not clear that the PSF-fitting 
  only approach would be slower, given that the matched filter requires a convolution as   well as something with the accuracy of PSF-fitting to estimate flux.

Our response:

We do not wish to argue against PSF-fitting for speed reasons. We only want to argue that for the purpose of centroiding stars, 
fast and approximate methods such as matched-filter polynomial centroiding (and in some cases the fixed Gaussian polynomial method) 
can be as efficient as PSF-fitting in terms of saturating the CRLB. But we agree with the referee that the way section 6, paragraph 6 was written 
may imply that we are arguing against use of PSF-fitting. 

  Referee comment:

  - Section 6, paragraphs 7-8: These paragraphs are hard to follow, as many readers won't equate functions on values in 2D images to dot-products between 1D vectors without some explanation. 
  An equation or two would be helpful,   for example
  chi^2 = [ F^2 dot(PSF,PSF) - 2*F*dot(PSF,image) + dot(PSF,image) ] / sigma^2,
  and that the first and third terms are more or less constant when varying only the centroid, thus a chi^2 minimization is equivalent to finding the maximum of the match-filtered image.

Our response:

We have added equation (30) to clarify our point. This is now discussed in paragraphs 10 and 11 of the last section. 
The equation is added to paragraph 10. In paragraph 11, we explain how optimizing the modified chi-squared 
is equivalent to finding the peak of the matched-filter. 

  Referee comment:

  - Section 6, paragraph 10: It should be noted that estimation of a PSF within a few tenths of a pixel is trivial from most images. 
  Thus, when dealing with realistic images, there is little if any difference between a true   matched filter and the default polynomial.

Our response:

We agree with the referee comment. The discussion is now included in paragraph 13 of this section. For many images, theres is very 
little difference between a true  matched filter and the fixed-Gaussian polynomial centroiding method. Therefore, in paragraph 13 of 
section 6, we first mention that PSF-fitting always saturates the CRLB, but in most cases a simple polynomial centroiding after 
convolving the image with a fixed-Gaussian kernel would perform as good (in terms of saturating the CRLB) as the case where we do 
know the PSF at the positions of stars. That is, there is little difference between the performance of a matched-filter and a fixed-Gaussian 
polynomial centroiding. 


  Referee comment:

  - Figures: Is the Y-axis the error in the total centroid position (e.g., sqrt(dx^2+dy^2), or just the error in one axis? Given the derivation of the CRLB, I believe it to be one axis.

Our response:

We are sorry for not clarifying this. The Y-axis of the plots only show error in one axis. 
Furthermore, we have changed the Y-axis of the plots to the ratio between the x component of the 
centroiding error and the CRLB. We have clarified this in the captions of figures, the first paragraph of 
subsection 5.1, and the first paragraph of the subsection 5.2 .

  Referee comment:

  - Figures: Log-log plots have the ability to make the errors look smaller than they are. The authors may wish to consider plotting with (error/CRLB) on the Y axis.

Our response:

We agree with th referee and we have made relevant changes to the plots. 
We have changed the Y-axis to the ratio of error (in x-axis of the centroid positions) 
to the CRLB. We have removed the logarithmic scale of the Y-axis in all of the plots.

  Referee comment:

  - Figures 4 and 8: It seems that the use of a 17x17 postage stamp is artificially reducing the error at low SNR, given the large number of points with centroid errors near the limit of 7-8 pixels.
  
Our response:
  
The 7x7 moment methods fails to return reliable centroiding methods in the limit of low signal-to-noise ratio. 
As a result, we see a large number of outliers that correspond to centroiding errors near the limit of 7-8 pixels.
In the end of the 5th paragraph of section 6, we explicitly mention that in the case of SNR = 5, the errors arising from the 
7x7 moment method are suppressed by the fact that 17x17 postage-stamps are used to simulate images. 
We also add that we expect the deviation of the RMSE from the CRLB to be larger for this method.
  
In addition to the changes given above, we also made the following
small changes:

* Added references to Foreman-Mackey et al. 2015, Rowe et al. 2015, 
and Zuntz et al. 2013, 2014.  

* Fixed a few typos.

* We have changed the color of plots.  

* Added some acknowledgements, including one to the referee.

