from PyQt5 import QtCore, QtGui, QtWidgets
import os
import praw 
import prawcore
import json
from datetime import datetime
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(621, 446)
        base_path = os.path.dirname(os.path.abspath(__file__))  
        image_path = os.path.join(base_path, "images/reddit.ico")
        MainWindow.setWindowIcon(QtGui.QIcon(image_path))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FF3D0C;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 131, 71))
        self.label_2.setText("")
        base_path = os.path.dirname(os.path.abspath(__file__))  
        image_path = os.path.join(base_path, "images/reddit.png")
        self.label_2.setPixmap(QtGui.QPixmap(image_path))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.home_widget = QtWidgets.QWidget(self.centralwidget)
        self.home_widget.setGeometry(QtCore.QRect(10, 90, 601, 351))
        self.home_widget.setObjectName("home_widget")
        self.pushButton = QtWidgets.QPushButton(self.home_widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius:5px;\n"
"background-color:#070F2B;\n"
"color:#fff;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.request_thread)
        self.lineEdit = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 100, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.widget = QtWidgets.QWidget(self.home_widget)
        self.widget.setGeometry(QtCore.QRect(310, 20, 261, 311))
        self.widget.setStyleSheet("background-color:#070F2B;\n"
"border-radius:5px;")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#fff;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#fff;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#fff;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#fff;")
        self.label_6.setObjectName("label_6")
        self.subreddit_ui = QtWidgets.QLabel(self.widget)
        self.subreddit_ui.setGeometry(QtCore.QRect(110, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.subreddit_ui.setFont(font)
        self.subreddit_ui.setStyleSheet("color:#FF3D0C;")
        self.subreddit_ui.setObjectName("subreddit_ui")
        self.posts_len_ui = QtWidgets.QLabel(self.widget)
        self.posts_len_ui.setGeometry(QtCore.QRect(120, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.posts_len_ui.setFont(font)
        self.posts_len_ui.setStyleSheet("color:#FF3D0C;")
        self.posts_len_ui.setObjectName("posts_len_ui")
        self.comments_len_ui = QtWidgets.QLabel(self.widget)
        self.comments_len_ui.setGeometry(QtCore.QRect(160, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.comments_len_ui.setFont(font)
        self.comments_len_ui.setStyleSheet("color:#FF3D0C;")
        self.comments_len_ui.setObjectName("comments_len_ui")
        self.label_7 = QtWidgets.QLabel(self.home_widget)
        self.label_7.setGeometry(QtCore.QRect(40, 300, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#FF3D0C;")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.home_widget)
        self.label_12.setGeometry(QtCore.QRect(140, 300, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:#070F2B;")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(110, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#070F2B;")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reddit Scrapper By Mossab H."))
        self.label.setText(_translate("MainWindow", "Reddit"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.lineEdit.setToolTip(_translate("MainWindow", "Subreddit name"))
        self.lineEdit.setText(_translate("MainWindow", "Investing"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Subreddit"))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "number of posts you want to get"))
        self.lineEdit_3.setText(_translate("MainWindow", "50"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Limit"))
        self.label_3.setText(_translate("MainWindow", "message"))
        self.label_4.setText(_translate("MainWindow", "Subreddit: "))
        self.label_5.setText(_translate("MainWindow", "Total Posts:"))
        self.label_6.setText(_translate("MainWindow", "Total Comments:"))
        self.subreddit_ui.setText(_translate("MainWindow", ""))
        self.posts_len_ui.setText(_translate("MainWindow", ""))
        self.comments_len_ui.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "Developed by:"))
        self.label_12.setToolTip(_translate("MainWindow", "find me on upwork"))
        self.label_12.setText(_translate("MainWindow", "Mossab Hamici"))
        self.label_11.setText(_translate("MainWindow", "Scraper"))

    def request_thread(self):
        # Create and start a thread
        self.thread = threading.Thread(target=self.start)
        self.thread.start()

    def start(self):
        try:
            subreddit_input = self.lineEdit.text()
            posts_limit = int(self.lineEdit_3.text())
            self.subreddit_ui.setText(str(subreddit_input))
            self.posts_len_ui.setText("")
            self.comments_len_ui.setText("")
            self.label_3.setText("program started..")
            with open("./Data/config.json") as f:
                config = json.load(f)


            reddit = praw.Reddit(
                client_id = config["client_id"],
                client_secret = config["SECRET_KEY"],
                user_agent = config["user_agent"],
            )

            # Target subreddit
            subreddit = reddit.subreddit(subreddit_input)

            # Prepare data for JSON
            posts_data = []
            
            # Extract image URL from the post
            def get_image_url(post):
                # Case 1: Direct image links (URL ends with an image extension)
                if post.url.endswith(('.jpg', '.png', '.gif')):
                    return post.url
                
                # Case 2: Reddit-hosted media with a preview image
                if hasattr(post, "preview") and "images" in post.preview:
                    return post.preview["images"][0]["source"]["url"]
                
                # Case 3: Gallery posts
                if hasattr(post, "gallery_data") and hasattr(post, "media_metadata"):
                    image_urls = []
                    for item in post.gallery_data["items"]:
                        media_id = item["media_id"]
                        if media_id in post.media_metadata:
                            media = post.media_metadata[media_id]
                            if "s" in media and "u" in media["s"]:
                                image_urls.append(media["s"]["u"])
                    return image_urls  # Return a list of gallery image URLs
                
                # Case 4: No image found
                return None
            
            # Fetch the first 10 posts
            for post in subreddit.hot(limit=posts_limit):  
                # Check if the post URL is from Reddit
                if "reddit.com" not in post.url:
                    # Convert the URL to the Reddit post permalink format
                    post_url = f"https://www.reddit.com/r/worldnews/comments/{post.id}/"
                else:
                    post_url = post.url
                    
                # Get the image URL
                image_url = get_image_url(post)
                    
                post_dict = {
                    "post_id": post.id,
                    "post_title": post.title,
                    "post_body": post.selftext,
                    "post_url":post_url,
                    "image_url": image_url,
                    "comments": []
                }
                # Fetch comments
                post.comments.replace_more(limit=None)  # Remove "load more comments"
                top_comments = post.comments[:50]  # Limit to top 50 comments
                for comment in top_comments:
                    comment_dict = {
                        "comment_id": comment.id,
                        "comment_body": comment.body,
                        "replies": []
                    }
                    
                    # Recursive function to fetch all replies
                    def get_replies(comment, depth=1):
                        replies = []
                        for reply in comment.replies:
                            reply_dict = {
                                "reply_id": reply.id,
                                "reply_body": reply.body,
                                "depth": depth
                            }
                            # Fetch deeper replies recursively
                            reply_dict["replies"] = get_replies(reply, depth + 1)
                            replies.append(reply_dict)
                        return replies

                    comment_dict["replies"] = get_replies(comment)
                    post_dict["comments"].append(comment_dict)
                
                posts_data.append(post_dict)

            # Save to JSON file
            today = datetime.today().strftime("%Y-%m-%d")
            output_file = f"{str(subreddit_input)} {today}.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(posts_data, f, indent=4, ensure_ascii=False)

            # Function to count all comments and replies
            def count_comments(comments):
                total = 0
                for comment in comments:
                    total += 1
                    if "replies" in comment and isinstance(comment["replies"], list):
                        total += count_comments(comment["replies"])
                return total
            num_titles = len(posts_data)
            num_comments = sum(count_comments(post["comments"]) for post in posts_data)
            self.posts_len_ui.setText(str(num_titles))
            self.comments_len_ui.setText(str(num_comments))
            self.label_3.setText(f"saved to {output_file}")
            print(f"Data saved to {output_file}")
        except prawcore.exceptions.NotFound as e:
            print("Error: Subreddit not found or does not exist.")
            self.label_3.setText("Error: Subreddit doesn't exist.")
            print(f"Details: {e}")
        except ValueError:
            self.label_3.setText("Error:Please enter an integer.")
            
        except Exception as e:
            print("An unexpected error occurred.")
            self.label_3.setText("Error: Try again")
            print(f"Details: {e}")
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
