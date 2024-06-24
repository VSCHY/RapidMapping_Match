# RapidMapping_Match
Tool to match rapid mapping locations from Copernicus to specific locations, and postal code for Germany. 


Data from a specific event can be found in : [https://emergency.copernicus.eu/mapping/list-of-activations-rapid](https://emergency.copernicus.eu/mapping/list-of-activations-rapid)

For now it is only built to process flood type of event. And postal code assessment is only available for Germany.

### How to 

1. The dataset must be extracted in DATA in a folder with the reference (e.g. EMSR728) and all zip file must be extracted there.

2. Then the preprocess must be launch with the bash file using the reference of the event:

```bash
bash launch_preprocess.bash EMSR728
```

3. This will generate two set of file, one with exact shapes and one with the postal code affected (only applicable for Germany for now).

4. Then the assessment can be run, an example on the different existing solutions that can be used is available un **run_assessment_example.py**. It contains 3 possible solutions:
  - assess based on precise coordinates
  - assess based on a postal code (only for Germany)
  - if a coordinates is available but only represent the location of the administrative unit (not precise location of the asset), it it possible to retrieve the postal code to be able to further perform the assessment based on the postal code. 
