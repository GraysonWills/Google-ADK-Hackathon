import subprocess
import pprint as pp


def detect_video():
    try:
        # Run ffprobe to get video information
        cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', 
                '-show_entries', 'stream=width,height,duration', 
                '-of', 'json', 'test.mov']
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Video file 'test.mov' detected successfully")
            pp.pprint(result.stdout)
            return True
        else:
            print("Video file 'test.mov' not found or invalid")
            return False
            
    except FileNotFoundError:
        print("FFmpeg/FFprobe is not installed or not in system PATH")
        return False
    except Exception as e:
        print(f"Error detecting video: {str(e)}")
        return False

if __name__ == "__main__":
    detect_video()