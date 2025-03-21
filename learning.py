
























import mysql.connector
from mysql.connector import Error
import cv2
import os

# Connect to MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="user"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def sign_up(username, password):
    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        query = "INSERT INTO user_info (username, password) VALUES (%s, %s)"
        values = (username, password)
        try:
            cursor.execute(query, values)
            connection.commit()
            return "Sign-up successful!"
        except Error as e:
            return f"Error: {e}"
        finally:
            cursor.close()
            connection.close()

def sign_in(username, password):
    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        query = "SELECT * FROM user_info WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return "Sign-in successful!"
        else:
            return "Invalid credentials. Please try again."

# def play_course_video():
    
#     video_path = r'C:/Users/admin/OneDrive/Desktop/Project/IEEE/vedios/I am sorry.mp4'  # Change this to your actual video file path

#     if not os.path.exists(video_path):
#         print("Video file not found!")
#         return

#     cap = cv2.VideoCapture(video_path)

#     if not cap.isOpened():
#         print("Error: Could not open video file")
#         return

#     # Get the frame rate of the video
#     fps = cap.get(cv2.CAP_PROP_FPS)

#     # Calculate the number of frames to display for 2 seconds
#     frames_to_play = int(fps * 2)  # 2 seconds

#     # Play the video for the specified duration
#     for _ in range(frames_to_play):
#         ret, frame = cap.read()
#         if not ret:
#             break  # Stop if the video ends before 2 seconds

#         cv2.imshow('Video Display', frame)

#         # Wait for a short period of time to show the frame
#         cv2.waitKey(int(1000 / fps))  # Delay based on frame rate

#     # Release the video capture and close the window
#     cap.release()
#     cv2.destroyAllWindows()
#     print("Video display finished.")















# def play_course_video(self, video_path):
#     # Check if the file exists
#     if not os.path.exists(video_path):
#         self.show_dialog("Video file not found!")
#         return

#     cap = cv2.VideoCapture(video_path)

#     if not cap.isOpened():
#         self.show_dialog("Error: Could not open video file")
#         return

#     # Get the frame rate of the video
#     fps = cap.get(cv2.CAP_PROP_FPS)

#     # Calculate the number of frames to display for 2 seconds
#     frames_to_play = int(fps * 2)  # 2 seconds

#     # Play the video for the specified duration
#     for _ in range(frames_to_play):
#         ret, frame = cap.read()
#         if not ret:
#             break  # Stop if the video ends before 2 seconds

#         cv2.imshow('Video Display', frame)

#         # Wait for a short period of time to show the frame
#         cv2.waitKey(int(1000 / fps))  # Delay based on frame rate

#     # Release the video capture and close the window
#     cap.release()
#     cv2.destroyAllWindows()
#     self.show_dialog("Video display finished and your scorecard is updated")












# def play_course_video(self, video_path):
#     print(f"Playing video: {video_path}")  # Debugging line

#         # Check if the file exists
#     if not os.path.exists(video_path):
#         self.show_dialog("Video file not found!")
#         return

#     cap = cv2.VideoCapture(video_path)  # This line needs cv2 to be imported

#     if not cap.isOpened():
#         self.show_dialog("Error: Could not open video file")
#         return

#     # Play the video until it ends
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break  # Stop if the video ends

#         cv2.imshow('Video Display', frame)
#         cv2.waitKey(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

#     cap.release()
#     cv2.destroyAllWindows()
#     self.show_dialog("Video display finished.")














# import threading

def play_course_video(self, video_path):
    def play_video():
        print(f"Playing video: {video_path}")  # Debugging line

        if not os.path.exists(video_path):
            self.show_dialog("Video file not found!")
            return

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            self.show_dialog("Error: Could not open video file")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video Display', frame)
            cv2.waitKey(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

        cap.release()
        cv2.destroyAllWindows()
        self.show_dialog("Video display finished.")

    # Start the video playback in a new thread
    threading.Thread(target=play_video).start()





#learning.py

import mysql.connector

def fetch_courses():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='user'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT course_name, video_path FROM courses")
    courses = cursor.fetchall()

    print(f"Fetched courses: {courses}")  # Debugging line

    cursor.close()
    connection.close()
    return courses

# Other functions (sign_up, sign_in, etc.) go here
