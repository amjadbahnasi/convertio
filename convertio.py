# To run the script run pip install moviepy.
# Change the frame by edit fps.
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(mp4_file, gif_file, fps=10, scale=None):
    clip = VideoFileClip(mp4_file)
    if scale:
        clip = clip.resize(scale)
    clip.write_gif(gif_file, fps=fps, program='ffmpeg', opt='optimizeplus')
    clip.close()

# Example usage
mp4_file = 'gif.mp4'
gif_file = 'output2.gif'
convert_mp4_to_gif(mp4_file, gif_file, fps=24)
