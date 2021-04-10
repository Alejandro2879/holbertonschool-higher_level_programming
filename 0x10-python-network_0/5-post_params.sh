#!/bin/bash                                                                                                                                     
# Script that takes in a URL, sends a POST request to the passed URL                                                                            
curl "$1" -s -d "email: hr@holbertonschool.com&subject: I will always be here for PLD" 
