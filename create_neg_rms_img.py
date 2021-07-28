def create_neg_rms_img(sci_img, wht_img, neg_out, rms_out, fix_nan, fix_inf, set_img):

    '''
    \n
    \nWelcome to create_neg_rms_img!

    This function is designed to take user
    provided science and weight FITS images,
    calculate negative and root mean square
    results, and save them as new FITS files.

    The function parameters are:

    sci_img: filename of your input science image
    wht_img: filename of your input weight image
    neg_out: desired filename of your negative image
    rms_out: desired filename of your rms image
    fix_nan: replace NaNs with zero (True or False)
    fix_inf: replace Infs with 1e10 (True or False)
    set_img: create SExtractor images (True or False)

    Notes:
     - All filenames should be entered as strings.
     - The code assumes data are in extension [0].
     - pixreplace may freeze for large files when
     there is insufficient memory and the function
     may be run in a new jupyter kernel or terminal.

    Written by Mitchell Revalski
    Last Updated on February 18, 2021
    Contributions by Laura Prichard and Marc Rafelski
    '''

    # History:
    # Created on June 9, 2020
    # Updated on July 13, 2020
    # - added commands to close the fits files.
    # - added NaN+Inf replacement for SCI and WHT.
    # Updated on October 27, 2020
    # - added set_img for Source Extractor compatibility.
    # - removes the problematic headlets but also the WCS.
    # Updated on February 18, 2021
    # - modified writeto in set_img to save WCS header.
    # - corrected minor typographical errors in notes.

    print('Calling create_neg_rms_img()...')

    # Import packages
    import numpy
    from astropy.io import fits
    from drizzlepac import pixreplace

    # Open the SCI image
    sci_hdul = fits.open(sci_img)
    sci_data = sci_hdul[0].data

    # Open the WHT image
    wht_hdul = fits.open(wht_img)
    wht_data = wht_hdul[0].data

    # Generate the NEG image
    print('\nCalculating negative image...')
    neg_img = (-1.0*sci_data)

    # Generate the RMS image
    print('\nCalculating rms image...\n')
    rms_img = (1.0/numpy.sqrt(wht_data))

    # Replace the data arrays
    sci_hdul[0].data = neg_img
    wht_hdul[0].data = rms_img

    # Export the images
    sci_hdul.writeto(neg_out, overwrite=True)
    wht_hdul.writeto(rms_out, overwrite=True)

    # Replace NaNs if selected
    if fix_nan == True:
        pixreplace.replace(sci_img)
        pixreplace.replace(wht_img)
        pixreplace.replace(neg_out)
        pixreplace.replace(rms_out)

    # Replace Infs if selected
    if fix_inf == True:
        pixreplace.replace(sci_img, pixvalue=numpy.inf, newvalue=1.0e10)
        pixreplace.replace(wht_img, pixvalue=numpy.inf, newvalue=1.0e10)
        pixreplace.replace(neg_out, pixvalue=numpy.inf, newvalue=1.0e10)
        pixreplace.replace(rms_out, pixvalue=numpy.inf, newvalue=1.0e10)

    # Close the images
    sci_hdul.close()
    wht_hdul.close()

    # Create Source Extractor images
    if set_img == True:

        # Open the images
        sci_hdul = fits.open(sci_img)
        wht_hdul = fits.open(wht_img)
        neg_hdul = fits.open(neg_out)
        rms_hdul = fits.open(rms_out)

        # Write only the first extension for Source Extractor.
        fits.writeto(sci_img, sci_hdul[0].data, sci_hdul[0].header, overwrite=True)
        fits.writeto(wht_img, wht_hdul[0].data, wht_hdul[0].header, overwrite=True)
        fits.writeto(neg_out, neg_hdul[0].data, neg_hdul[0].header, overwrite=True)
        fits.writeto(rms_out, rms_hdul[0].data, rms_hdul[0].header, overwrite=True)

        # Close the images
        sci_hdul.close()
        wht_hdul.close()
        neg_hdul.close()
        rms_hdul.close()

    # Print completion
    print('\nDone.')

# End of function
