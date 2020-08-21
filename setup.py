import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="augment_auto",
    version="0.1.0",
    author="keshav sharma",
    author_email="keshavoct98@gmail.com",
    description="An image augmentation library for object detection and image classification tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keshavoct98/image-augmentation",
    packages=['augment'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='augment, augmentation, image, object, sampling',
    install_requires = ['opencv-python>=4.1.1', 'numpy>=1.19.0']
)
