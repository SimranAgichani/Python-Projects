Summary
Automated the manual defect inspection process for casting manufacturing products by using Keras CNNs in Python to analyze and classify top-view grayscale pump images, achieving 95% accuracy and potentially preventing order rejections

Context
This dataset is of casting manufacturing product.
Casting is a manufacturing process in which a liquid material is usually poured into a mold, which contains a hollow cavity of the desired shape, and then allowed to solidify.
Reason for collect this data is casting defects!!
casting defect is an undesired irregularity in a metal casting process.
There are many types of defect in casting like blow hole, pin hole, burr,shrinkage defects, mold material defects, pouring metal defects, metallurgical defects, etc.
Defects are unwanted thing in casting industry.For removing this defective product all industry have their quality inspection department. But main problem is this inspection process is carried out manually. It is very time consuming process and due to human accuracy this is not 100% accurate.This can be cause of rejection of whole order. So it create big loss in company.

We decided to make inspection process automatic and for this we need to make deep learning classification model for this problem.
There are main two categories:-
1. Defective
2. Ok

These all photos are top view of submersible pump impeller(google search for better understanding).
The dataset contains total 7348 image data.These all are size of (300*300) pixels gray scaled images.

