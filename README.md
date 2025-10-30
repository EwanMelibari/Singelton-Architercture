# Python Singleton Logging Service

## Overview: The Problem & The Pattern

This project implements a robust, single-instance **Logging Service** for Python applications, utilizing the **Singleton** design pattern.

### What is the Singleton Pattern?

The **Singleton** is a creational design pattern that guarantees a class has **only one instance** throughout the application's lifecycle, while providing a global point of access to that instance. 

### Why Use Singleton for Logging?

When managing shared resources like logging, you need guaranteed consistency. The Singleton pattern solves two critical problems:

1.  **Enforce Uniqueness:** Prevents the creation of multiple, separate logging configurations. You never have to worry about accidentally spawning a second logger that misses some of your application's events.
2.  **Centralized Access:** Provides a single, global access point (`LoggingService()`) that all parts of your application—from different modules to threads—can reliably call to log messages.

---

## ⚙️ Implementation Strategy (The Python Magic)

The entire Singleton behavior is enforced by overriding the special **`__new__`** method, which is the class constructor responsible for creating the instance.

* **The Gatekeeper `__new__`**:
    * It checks the class-level attribute `_instance`.
    * If the instance is not yet created (`_instance is None`), it creates the new object and performs the expensive, **one-time setup** (configuring file and console handlers, setting the level).
    * For all subsequent calls to `LoggingService()`, it simply returns the already existing `_instance`, ensuring setup logic is never duplicated.

* **Instance Setup**: The actual Python logger (`logging.Logger`) is created and attached as an instance attribute (`cls._instance._logger`), while the Singleton reference (`cls._instance`) is a class attribute—a subtle but important distinction for correct implementation.

---

## 📐 Class Diagram

This diagram visualizes how the class manages its own singular instance.

![Class Diagram for the Singleton Logging Service](https://github.com/EwanMelibari/Singelton-Architercture/blob/main/Logging%20service%20class%20Diagram-Page-1.drawio.png)

---

## 🚀 Usage and Verification

The code below demonstrates that two seemingly separate instances (`logger1` and `logger2`) are, in fact, references to the exact same object, confirming the Singleton pattern.

**Code:**
```python
import logging
# Assume LoggingService class is defined here

# First call: Creates and configures the ONE instance
logger1 = LoggingService()
logger1.info("Logger 1: Application initialization starting...")

# Second call: Returns the previously created instance (setup is skipped)
logger2 = LoggingService(log_file="ignored.log", log_level=logging.DEBUG)
logger2.error("Logger 2: A simulated error was logged.")

# --- Verification ---

# 1. Identity Check
is_same = logger1 is logger2
print(f"Are logger1 and logger2 the same object? {is_same}") 
# Output: True

# 2. Memory ID Check (Concrete Proof)
print(f"Logger 1 ID: {id(logger1)}")
print(f"Logger 2 ID: {id(logger2)}")
# Output: Both IDs will be identical.
