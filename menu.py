import pygame
import os

#匯入圖片
MENU_IMAGES=pygame.image.load("images/upgrade_menu.png")
UPGRADE_IMAGES=pygame.transform.scale(pygame.image.load("images/upgrade.png"), (60, 30))
SELL_IMAGES=pygame.transform.scale(pygame.image.load("images/sell.png"), (40, 40))

class UpgradeMenu:
    def __init__(self, x, y):
        self.menu_image = pygame.transform.scale(MENU_IMAGES, (200, 200))  #引入 menu 的圖片,並設定大小
        self.rect = self.menu_image.get_rect()  #偵測 menu 的矩形範圍
        self.rect.center = (x, y)  #將給定的 x,y 設為 menu 的矩形中心座標
        #將 upgrade 和 sell 兩張圖片與其名稱、位置寫入 Button 的物件中,並放入 list 裡
        self.__buttons = [Button(UPGRADE_IMAGES, "upgrade", self.rect.centerx, self.rect.centery-75),
                          Button(SELL_IMAGES, "sell", self.rect.centerx, self.rect.centery+75)]  # (Q2) Add buttons here
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, (self.rect.centerx-100, self.rect.centery-100))  #將 menu 印到 win 上
        # draw button
        # (Q2) Draw buttons here
        win.blit(UPGRADE_IMAGES, (self.rect.centerx-32, self.rect.centery-86))  #將 upgrade 印到 win 上
        win.blit(SELL_IMAGES, (self.rect.centerx-20, self.rect.centery+55))  #將 sell 印到 win 上

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons  #回傳含有按鍵的 list
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name  #設定 button 的名字
        self.image = image  #設定 button 為哪張圖片
        self.rect = self.image.get_rect()  #偵測所用圖片的矩形範圍
        self.rect.center = (x, y)  #將給定的 x,y 設為圖片的矩形中心座標


    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint(x,y):  #若所點的位置在物件的矩形範圍內,回傳 True
            return True
        else:  #反之,回傳 False
            return False
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        if self.name == "upgrade":  #若 self.name 為 upgrade, 回傳字串 "upgrade"
            return "upgrade"
        elif self.name == "sell":  #若 self.name 為 sell, 回傳字串 "sell"
            return "sell"
        pass






