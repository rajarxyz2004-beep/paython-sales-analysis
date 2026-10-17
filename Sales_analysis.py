{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOC4Q2gsxWhWVIdaLOd1mTd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rajarxyz2004-beep/paython-sales-analysis/blob/main/Sales_analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KMoZlMC5PstQ",
        "outputId": "ea41aa9c-6bd0-40be-aa80-e1c244ba9dc5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- Python Sales Analysis Project ---\n",
            "\n",
            "Total Sales Amount: $135000\n",
            "Top Selling Category: Electronics ($45000)\n",
            "\n",
            "Category-wise Sales Breakdown:\n",
            "- Electronics: $45000\n",
            "- Clothing: $20000\n",
            "- Groceries: $15000\n",
            "- Appliances: $30000\n",
            "- Furniture: $25000\n"
          ]
        }
      ],
      "source": [
        "# Sample Sales Data: Categories and their total sales amount\n",
        "sales_data = {\n",
        "    \"Electronics\": 45000,\n",
        "    \"Clothing\": 20000,\n",
        "    \"Groceries\": 15000,\n",
        "    \"Appliances\": 30000,\n",
        "    \"Furniture\": 25000\n",
        "}\n",
        "\n",
        "print(\"--- Python Sales Analysis Project ---\\n\")\n",
        "\n",
        "# 1. Total Sales calculate panrom\n",
        "total_sales = sum(sales_data.values())\n",
        "print(f\"Total Sales Amount: ${total_sales}\")\n",
        "\n",
        "# 2. Highest sales edhula vandhurukku nu parkalam\n",
        "best_category = max(sales_data, key=sales_data.get)\n",
        "print(f\"Top Selling Category: {best_category} (${sales_data[best_category]})\")\n",
        "\n",
        "# 3. Category wise breakdown print panrom\n",
        "print(\"\\nCategory-wise Sales Breakdown:\")\n",
        "for category, amount in sales_data.items():\n",
        "    print(f\"- {category}: ${amount}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "NsQF85nIP3BW"
      }
    }
  ]
}