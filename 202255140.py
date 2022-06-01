{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jkim2397/ayou/blob/main/202255140.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lTT7vMUiif25"
      },
      "outputs": [],
      "source": [
        "import csv\n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "url =\"https://comic.naver.com/webtoon/weekday\"\n",
        "\n",
        "\n",
        "filename = \"네이버 웹툰 인기 순위.csv\"\n",
        "f = open(filename, \"w\", encoding=\"utf-8-sig\", newline=\"\")\n",
        "writer = csv.writer(f)\n",
        "\n",
        "columns_name = [\"순위\", \"웹툰명\"] \n",
        "\n",
        "writer.writerow(columns_name)\n",
        "\n",
        "\n",
        "res = requests.get(url)\n",
        "res.raise_for_status()\n",
        "\n",
        "\n",
        "soup = BeautifulSoup(res.text, \"lxml\")\n",
        "cartoonsBox = soup.find('ol', attrs={\"class\": \"asideBoxRank\"}) \n",
        "cartoons = cartoonsBox.find_all('a') \n",
        "\n",
        "\n",
        "for cartoon in cartoons: \n",
        "  \n",
        "  title = cartoon.get(\"title\") \n",
        "  \n",
        "  \n",
        "  i=int(input(\"순위를 입력하세요 :\"))\n",
        "  data = [str(i), title]\n",
        "  writer.writerow(data)\n",
        "  print(cartoons[i-1].get_text())\n",
        "  "
      ]
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "name": "202255140-소예훈.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPbHVd9/KehtYQrxm3wQFaT",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}