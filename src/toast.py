"""Notify you after the script running done."""

import platform
from pathlib import Path

from windows_toasts import WindowsToaster, Toast, ToastDisplayImage, ToastImagePosition

from src.config import settings
from src.log import logger


class Toaster:
    def __init__(self, title: str = settings.project.name, body: str = "Done", logo: Path = None):
        self._title = title
        self._body = body
        self._logo = logo

    def _windows(self):
        """actually, win10 & win11"""
        toast_main = WindowsToaster(applicationText=self.title)
        logo = ToastDisplayImage.fromPath(self.logo)
        logo.position = ToastImagePosition.AppLogo
        toast_body = Toast(
            text_fields=[self.body],
            images=[logo]
        )
        toast_main.show_toast(toast_body)

    def _macos(self):
        """TODO"""
        logger.info("Sorry babe, MacOS notification has not been implemented yet :)")

    def _linux(self):
        """TODO"""
        logger.info("Sorry babe, Linux notification has not been implemented yet :)")

    def notify(self):
        match platform.system().lower():
            case "windows":
                return self._windows()
            case "macos":
                return self._macos()
            case "linux":
                return self._linux()
            case _:
                raise NotImplementedError

    @property
    def title(self) -> str:
        return self._title

    @property
    def body(self) -> str:
        return self._body

    @property
    def logo(self) -> Path:
        return self._logo


__all__ = [
    "Toaster",
]
