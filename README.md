# create_neg_rms_images

Jupyter Notebook that calculates RMS and NEG images from user-supplied SCI and WHT drizzles.

This Jupyter Notebook was created by Dr. Mitchell Revalski to generate negative (NEG) and root-mean-square (RMS) images from user-supplied Hubble Space Telescope (HST) Wide Field Camera 3 (WFC3) science (SCI) and inverse variance weight map (WHT) drizzles that were produced with [DrizzlePac's](https://www.stsci.edu/scientific-community/software/drizzlepac.html) [AstroDrizzle](https://drizzlepac.readthedocs.io/en/latest/astrodrizzle.html) software. These images are useful for determining detection thresholds and estimating noise properties when measuring the photometry of objects in the SCI image with [Source Extractor](https://www.astromatic.net/software/sextractor/) and similar codes. The code is specifically designed to use WHT maps that were generated with `final_wht_type='IVM'`.

If you prefer to run the code as a terminal script, you can use `create_neg_rms_img.py` and print the codes help message using:

`python -c "import create_neg_rms_img; help(create_neg_rms_img)"`

The basic call sequence where the first four arguments are replaced with your corresponding filenames is then:

`python -c "import create_neg_rms_img; create_neg_rms_img.create_neg_rms_img('sci_img', 'wht_img', 'neg_out', 'rms_out', True, True, False)"`

Please send questions, comments, and suggestions to [Mitchell Revalski](https://www.mitchellrevalski.com). Thank you, and have a nice day!

Mitchell Revalski gratefully acknowledges Laura Prichard and Marc Rafelski for helping to improve this code.
