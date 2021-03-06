# Singly Linked List
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

## Challenge
- Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
![image](../assets/linkedLists.png)

---

**Insert before and after method**

![image](../assets/linkedLists-kth.png)

---

**Kth value**

![image](../assets/linkedLists-ins.png)

## Big O

Time - O(n)

Space - O(1)

---
REF: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/\
Author: John Shiver
---

## API