# This project is a toy project for training and quality assurance purposes

# Day 2

Given this data from customer feedback, implement flask api that uses the following decision tree algorithm to figure out recommendation based on the inputs. 

Decision tree algorithms random forest, ID3, CART, adaboost.

DO NOT USE OPEN AI

data = '''
Preference Red_Wine White_Wine Recommendation
Red Light-Bodied None Pinot Noir
Red Full-Bodied None Shiraz or Zinfandel
White None Dry Sauvignon Blanc
White None None Sweet Gewurztraminer
Red-Fruity None None Pinot Noir
Red-Earthy None None Chianti
White-Crisp None None Sauvignon Blanc
White-Creamy None None Chardonnay
Red-Spicy None None Shiraz or Zinfandel
Red-Rich None None Cabernet Sauvignon
White-Floral None None Gewurztraminer
White-Citrus None None Riesling
Red None None Pinot Noir
Red None None Chianti
White None None Sauvignon Blanc
White None None Chardonnay
Red None None Shiraz or Zinfandel
Red None None Cabernet Sauvignon
White None None Gewurztraminer
White None None Riesling
Red-Fruity Light-Bodied None Pinot Noir
Red-Fruity Full-Bodied None Shiraz or Zinfandel
Red-Earthy Light-Bodied None Pinot Noir
Red-Earthy Full-Bodied None Cabernet Sauvignon
White-Crisp Dry None Sauvignon Blanc
White-Crisp Sweet None Pinot Noir
White-Creamy Dry None Pinot Noir
White-Creamy Sweet None Chardonnay
Red-Spicy Light-Bodied None Pinot Noir
Red-Spicy Full-Bodied None Shiraz or Zinfandel
Red-Rich Light-Bodied None Pinot Noir
Red-Rich Full-Bodied None Cabernet Sauvignon
White-Floral Dry None Pinot Noir
White-Floral Sweet None Gewurztraminer
White-Citrus Dry None Sauvignon Blanc
White-Citrus Sweet None Riesling
Red-Fruity None Sweet Pinot Noir
Red-Fruity None Dry Pinot Noir
Red-Earthy None Sweet Chianti
Red-Earthy None Dry Pinot Noir

Based on the data generate 10 different choices and recommended based on the choices
'''
