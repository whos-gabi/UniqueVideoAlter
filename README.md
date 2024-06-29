# UniqueVideoAlter

UniqueVideoAlter is a Python script that processes `.mp4` video files by slightly altering their brightness and modifying a single pixel in the first frame to make each video unique. The script ensures the original audio is preserved and deletes the original video after processing.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/whos-gabi/UniqueVideoAlter.git
   cd UniqueVideoAlter
2. **Ensure you have Python 3.11 installed**
    ```bash
    python3.11 --version
3. **Create and activate a virtual environment**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
4. **Install required packages**
    ```bash
    pip install -r requirements.txt
- If you don't have a requirements.txt file, you can create one with the following contents:
    ```bash
    moviepy
    numpy

## Usage

1. **Prepare your video files**

   Place all the `.mp4` video files you want to process into a single folder.

2. **Run the script**
   ```bash
   python main.py path/to/your/folder
- Replace path/to/your/folder with the actual path to the folder containing your .mp4 files.

## Example

Suppose your folder structure looks like this:
```
UniqueVideoAlter/
├── main.py
├── requirements.txt
└── videos/
    ├── video1.mp4
    ├── video2.mp4
    └── video3.mp4
```

- To process the videos in the videos folder, run:
    ```bash
    python main.py videos/

- After processing, the folder will contain:
    ```
    videos/
    ├── unique_video1.mp4
    ├── unique_video2.mp4
    ├── unique_video3.mp4
- The original videos will be deleted after processing.

