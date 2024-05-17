# Offer Man

**Version:** 0.1 Alpha  
**Release Date:** May 17, 2024  
**Author:** Albert Bozesan

---

## Introduction

This is Offer Man, a simple Llama3-8B-based project designed to help voiceover artists quickly decide on a rate to offer clients. This is an initial alpha release, version 0.1, which runs in Terminal on Mac.

## Installation

The following things must be installed to run Offer Man:
- Python3
- Ollama with the Llama3 8B parameter model.

## Running Offer Man

1. Place your rates in a file named `voiceover_rates.csv` in the same directory as `offerman.py`.

2. Simply run `offerman.py` in your Terminal with this command:
    ```bash
    python3 path/to/offerman.py
    ```

## Troubleshooting

- Make sure you have installed Ollama correctly. Check if it runs normally before attempting to run Offer Man.
- If you continue to get errors, check if your `voiceover_rates.csv` and the Model file are in the same directory as `offerman.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
