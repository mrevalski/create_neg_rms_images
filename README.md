# create_neg_rms_images

Jupyter Notebook that calculates RMS and NEG images from user-supplied SCI and WHT drizzles.

This Jupyter Notebook was created by Dr. Mitchell Revalski to generate negative (NEG) and root-mean-square (RMS) images from user-supplied Hubble Space Telescope (HST) Wide Field Camera 3 (WFC3) science (SCI) and inverse variance weight map (WHT) drizzles that were produced with [DrizzlePac's](https://www.stsci.edu/scientific-community/software/drizzlepac.html) [AstroDrizzle](https://drizzlepac.readthedocs.io/en/latest/astrodrizzle.html) software. These images are useful for determining detection thresholds and estimating noise properties when measuring the photometry of objects in the SCI image with [Source Extractor](https://www.astromatic.net/software/sextractor/) and similar codes. The code is specifically designed to use WHT maps that were generated with `final_wht_type='IVM'`.

Please send questions, comments, and suggestions to [Mitchell Revalski](https://www.mitchellrevalski.com). Thank you, and have a nice day!
