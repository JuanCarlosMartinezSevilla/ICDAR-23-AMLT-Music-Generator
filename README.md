# ICDAR 2023 Aligned Music Notation and Lyrics Transcription
## _Music Generator_

[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)]() [![Version](https://img.shields.io/static/v1?label=Version&message=1.0&color=)]() [![Python](https://img.shields.io/static/v1?label=Python&message=3.8.10&color=blue)]()

In this paper, we present the Aligned Music Notation and Lyrics Transcription (AMNLT) challenge, whose goal is to retrieve the content from document images of vocal music. This new research area arises from the need to automatically transcribe notes and lyrics from music scores and align both sources of information conveniently. Although existing methods are able to deal with music notation and text, they work without providing their proper alignment, which is crucial to actually retrieve the content of the piece of vocal music. To overcome this challenge, we consider holistic neural approaches that transcribe music and text in one step, along with an encoding that implicitly aligns the sources of information. The methodology is evaluated on a benchmark specifically designed for AMNLT. The results report that existing methods can obtain high-quality text and music transcriptions, but posterior alignment errors are inevitably found. However, our formulation achieves relative improvements of over 80\% in the metric that considers both transcription and alignment. We hope that this work will establish itself as a future reference for further research on AMNLT.

## Usage
Using this repository you will be able to generate synthethic musical fragments.

![generated_krn](https://github.com/JuanCarlosMartinezSevilla/ICDAR-23-AMNLT-Music-Generator/blob/main/examples/exampleCombined.png)

_Resultant .krn file rendered with Verovio Humdrum Viewer_

## Getting Started
Clone the repository:

```
git clone xxx
```

Install the dependencies:

```
pip install -r requirements.txt
```

## Citation
```bibtex
@inproceedings{,
    author    = {},
        title     = {},
        booktitle = {17th International Conference on Document Analysis and Recognition,
            {ICDAR}},
            series    = {},
            volume    = {},
            pages     = {},
            year      = {2023},
            doi       = {},
        }
```

## License

The MIT License (MIT)
