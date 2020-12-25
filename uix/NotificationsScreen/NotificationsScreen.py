from kivymd.uix.card import MDCardSwipe
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class Notification(MDCardSwipe):
    firstLine = StringProperty()
    secondLine = StringProperty()
    thirdLine = StringProperty()
    time = StringProperty()
    imageSource = StringProperty()

    def onSwipeComplete(self, notification):
        self.parent.remove_widget(notification)


class NotificationTime(IRightBodyTouch, MDLabel):
    pass


class NotificationsScreen(BoxLayout):

    def on_pre_enter(self):
        self.clearNotifications()
        self.addNotification('Бифидойогурт Черника-Инжир Активіа 270г', '24.80грн. -> 22.50грн.', 'Цена упала на 2.30грн.', '17:06', 'data/products/test.jpg')
        self.addNotification('Бифидойогурт Черника-Инжир Активіа 270г', '24.80грн. -> 22.50грн.', 'Цена упала на 2.30грн.', '16:40', 'data/products/test.jpg')
        self.addNotification('Бифидойогурт Черника-Инжир Активіа 270г', '24.80грн. -> 22.50грн.', 'Цена упала на 2.30грн.', '12:36', 'data/products/test.jpg')

    def on_pre_leave(self):
        self.clearNotifications()

    def clearNotifications(self):
        self.ids.notifications.clear_widgets()

    def addNotification(self, firstLine, secondLine, thirdLine, time, imageSource):
        notification = Notification()

        notification.firstLine = firstLine
        notification.secondLine = secondLine
        notification.thirdLine = thirdLine
        notification.time = time
        notification.imageSource = imageSource

        self.ids.notifications.add_widget(notification)


Builder.load_file('./uix/NotificationsScreen/NotificationsScreen.kv')
