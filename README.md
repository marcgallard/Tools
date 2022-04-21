<p align="center">
  <a href="https://github.com/mrcogllrdo/PixelShift">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/introImg.jpg" alt="PixelShift intro" width="630" height="354">
  </a>
</p>

<h3 align="center">PixelShift</h3>

![Version](https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![python](https://img.shields.io/badge/python-3.8-blue.svg?logo=python&labelColor=yellow)](https://www.python.org/downloads/)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/mrcogllrdo/PixelShift)

<p align="center">
  Image scrambler with stats for security and privacy purposes.
  <br>
  <a href="https://github.com/mrcogllrdo/PixelShift/blob/master/CHANGELOG.md"><strong>New Changes</strong></a>
  .
  <a href="https://github.com/mrcogllrdo/PixelShift/wiki"><strong>Check out the wiki!</strong></a>
</p>

## About PixelShift

PixelShift is an image viewer designed to scramble images such that they become unrecognizable after shared a certain number of times. The rate at which they deteriorate is customizable with a preview to ensure adequate scrambling. Each image is encrypted and signed before being shared with others alongside a header that contains relevant metadata.

The rationale behind PixelShift is that an image should not have the potential to be leaked with perfect reproducibility if it was only intended to be shared within a small group of people a handful of times. This is especially apparent when the image contains sensitive information. If the user is more concerned about getting an idea across versus the quality of the image then this software could be beneficial.

Stats such as standard deviation and cosine similarity score (more to come soon!) are included to see how much the scrambled image deviates from the original. This can always serve as a sanity check to see if an adversary can 1) trace the scrambled image to the original, 2) determine how many times it has been shared, 3) develop a map of when it was shared and with whom, et cetera.

Note current and planned features are open to change. For example, the cosine similarity score requires having the original and altered image, defeating the purpose of this software. Comparison techniques that only require one-way metadata of the original image (metadata and the image are not one-to-one; something akin to salting the image can guarantee this) are currently being investigated.

## Demo

Please feel free to check out the demo folder to see the program's current features without running it yourself. There's also a brief discussion for using one of the parameters to scramble your images over the other!

## Prerequisites

- NumPy for the stats-heavy operations
- Pip to make installing stuff like NumPy and Pillow easy (should come already with Python)
- Pillow for image manipulation

## Installation

Clone the repo: `git clone https://github.com/mrcogllrdo/PixelShift.git`

Then run

    pip install Pillow    
    
to install Pillow, and
    
    pip install numpy
    
to install NumPy.

We'll be using Tkinter for the GUI.

## Documentation

Please refer to the [wiki](https://github.com/mrcogllrdo/PixelShift/wiki).

## Copyright and license

Code and documentation copyright 2020 under [PixelShift's author](https://github.com/mrcogllrdo). Code released under the [AGPL v3.0 License](https://github.com/mrcogllrdo/PixelShift/blob/master/LICENSE). Documentation released under [Creative Commons](https://creativecommons.org/licenses/by/3.0/).

## Acknowledgements and Credits

Thanks to Pixabay for allowing me access to royalty-free pics.
