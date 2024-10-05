# yTwhisper

A **Python-based** tool to transcribe YouTube videos using **OpenAI's Whisper** model. This project facilitates the download of YouTube video audio, transcribes it into text, and saves the transcription for easy access and analysis.

## 📜 **Disclaimer and Compliance**

**Respecting YouTube's Terms of Service (ToS)** is of utmost importance. This project is intended **solely for research and educational purposes**. By using this tool, you agree to comply with YouTube's [Terms of Service](https://www.youtube.com/static?template=terms) and ensure that you have the necessary permissions to download and transcribe the content. Unauthorized downloading, redistribution, or commercial use of YouTube content violates YouTube's policies and may infringe on copyright laws.

**⚠️ Warning:**
- **Users**: Ensure you have explicit permission from content creators before downloading and transcribing their videos. Use this tool responsibly and ethically.
- **Contributors**: By contributing to this project, you agree to uphold these compliance standards and avoid facilitating any misuse of the tool that violates YouTube's ToS or applicable laws.

**Legal Notice:**
This software is provided "as-is", without any express or implied warranties. In no event will the authors be held liable for any damages arising from the use of this software.

## 🚀 **Features**

- **Download Audio**: Extracts audio from YouTube videos efficiently.
- **Transcribe with Whisper**: Utilizes OpenAI's Whisper model for accurate transcription.
- **Save Transcriptions**: Stores transcriptions in organized text files for easy access.
- **Portable and Open-Source**: Easily shareable and adaptable for various use cases.

## 🛠️ **Installation**

### **Prerequisites**

- **macOS 11.7 or higher**
- **Homebrew**: A package manager for macOS. [Install Homebrew](https://brew.sh/)
- **Conda**: An open-source package management and environment management system. [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)
- **GPU Support (Optional)**:
  - **Apple Silicon (M1, M2, etc.)**: To utilize GPU acceleration via Metal Performance Shaders (MPS).

### **Step-by-Step Setup**

1. **Clone the Repository**

    ```bash
    git clone git@github.com:dimasusername/ytwhisper.git
    cd ytwhisper
    ```

2. **Install FFmpeg via Homebrew**

    Although FFmpeg is included in the Conda environment, installing it via Homebrew can provide system-wide access, which might be beneficial for other applications.

    ```bash
    brew install ffmpeg
    ```

3. **Set Up the Conda Environment**

    **a. Create the Conda Environment**

    ```bash
    conda env create -f environment.yml
    ```

    **b. Activate the Environment**

    ```bash
    conda activate ytwhisper
    ```

    **c. Verify the Environment**

    Ensure that all dependencies are installed correctly.

    ```bash
    conda list
    ```

4. **Additional Recommendations**

    #### 4.1. Verify GPU Availability

    To ensure that your system is utilizing the GPU, you can add the following lines to your script to print device information:

    ```python
    import torch
    print("Torch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("MPS available:", torch.backends.mps.is_available())
    ```

## 🎯 **Usage**

Run the `main.py` script with the YouTube video URL as an argument:

```bash
python main.py "https://www.youtube.com/watch?v=your_video_id"
```

**Example:**

```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### **Output**

- **Audio File**: Saved in the `downloads/` directory.
- **Transcription**: Saved as a `.txt` file in the `transcriptions/` directory.

## **Troubleshooting**
If `yt-dlp` complains about ffmpeg location, test that ffmpeg actually works. [This thread](https://stackoverflow.com/questions/35509731/dyld-symbol-not-found-cg-jpeg-resync-to-restart) on SO may shed some light.

## 🧰 **Project Structure**

```
yTwhisper/
├── downloads
├── transcriptions
├── .gitignore
├── CODE_OF_CONDUCT.md
├── environment.yml
├── LICENSE
├── main.py
├── README.md
└── TERMS_OF_USE.md
```

- **downloads/**: Stores downloaded audio files (excluded from version control).
- **transcriptions/**: Stores the resulting transcription text files (excluded from version control).
- **main.py**: Main script to execute the transcription process.
- **requirements.txt**: Lists all Python dependencies.
- **README.md**: Project documentation.
- **.gitignore**: Specifies files and directories to ignore in version control.

## 🤝 **Contributing**

Contributions are welcome! Please adhere to the following guidelines:

1. **Respect Compliance Standards**: Ensure that any contributions do not facilitate the violation of YouTube's ToS or copyright laws.
2. **Code Quality**: Maintain clean, readable, and well-documented code.
3. **Submit Issues and Pull Requests**: Use GitHub's issue tracker for reporting bugs or suggesting features. Submit pull requests for proposed changes.

**To Contribute:**

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push to your fork and submit a pull request.

## 📄 **License**

This project is licensed under the [Apache License 2.0](LICENSE).

## 🧩 **Third-Party Licenses**

The **ytwhisper** project incorporates the following third-party libraries and tools, each governed by their respective licenses:

- **yt-dlp** - [Unlicense](https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE)
- **OpenAI Whisper** - [MIT License](https://github.com/openai/whisper/blob/main/LICENSE)
- **ffmpeg-python** - [MIT License](https://github.com/kkroening/ffmpeg-python/blob/master/LICENSE)
- **torch** - [BSD 3-Clause License](https://github.com/pytorch/pytorch/blob/master/LICENSE)
- **torchvision** - [BSD 3-Clause License](https://github.com/pytorch/vision/blob/main/LICENSE)
- **torchaudio** - [BSD 3-Clause License](https://github.com/pytorch/audio/blob/main/LICENSE)
- **numpy** - [BSD 3-Clause License](https://github.com/numpy/numpy/blob/main/LICENSE.txt)
- **ffmpeg** - [LGPLv2.1+ / GPLv3+ License](https://ffmpeg.org/legal.html)

## 📧 **Contact**

For questions, suggestions, or support, please open an issue on the [GitHub repository](https://github.com/dimasusername/ytwhisper/issues) or contact [dimasusername@proton.me](dimasusername@proton.me).

## 🌐 **Acknowledgements**

The **ytwhisper** project leverages a variety of open-source libraries and tools. Special thanks to the following projects and communities for making this tool possible:

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Advanced YouTube video downloader and extractor.
- **[OpenAI Whisper](https://github.com/openai/whisper)** - State-of-the-art speech recognition model.
- **[FFmpeg](https://ffmpeg.org/)** - Comprehensive multimedia framework for audio and video processing.
- **[Ollama](https://ollama.com/)** - Efficient model management and deployment tool.
- **[PyTorch](https://github.com/pytorch/pytorch)** - Flexible and powerful deep learning framework.
- **[Torchvision](https://github.com/pytorch/vision)** - PyTorch's computer vision library.
- **[Torchaudio](https://github.com/pytorch/audio)** - PyTorch's audio processing library.
- **[NumPy](https://github.com/numpy/numpy)** - Fundamental package for scientific computing with Python.

### 🙏 **Special Thanks To:**

- **The Open-Source Community**: For continuously contributing to and maintaining the libraries that power this project.
- **YouTube API and Developers**: For providing the tools that enable video data extraction and processing.
- **All Contributors**: Your feedback, suggestions, and code contributions have been invaluable in shaping this tool.

> **Note:**
> - **Ethical Use**: This tool is intended for **research and educational purposes**. Please ensure you have the necessary permissions to download and transcribe YouTube content.
> - **Compliance**: Always adhere to YouTube's [Terms of Service](https://www.youtube.com/static?template=terms) and respect content creators' rights.

EOF
