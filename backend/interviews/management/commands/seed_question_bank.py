from django.core.management.base import BaseCommand

from interviews.models import QuestionBank


class Command(BaseCommand):

    help = "Seeds the Question Bank with default interview questions."

    def handle(self, *args, **kwargs):

        questions = [
            # EASY (1-50)
            {"skill": "Python", "difficulty": "EASY", "question": "What is Python?"},
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What are Python's main features?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a variable in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "How do you declare a variable in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What are Python data types?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a list in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a tuple in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a dictionary in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a set in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is the difference between a list and a tuple?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is type casting in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "How do you take input from a user?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is the print() function?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What are comments in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is indentation in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a conditional statement?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "Explain if-else statements.",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a for loop?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a while loop?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is the range() function?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What are functions in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "How do you define a function?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What are function arguments?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a return statement?",
            },
            {"skill": "Python", "difficulty": "EASY", "question": "What is a module?"},
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "How do you import a module?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is the math module?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is exception handling?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is try-except?",
            },
            {"skill": "Python", "difficulty": "EASY", "question": "What is a string?"},
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What are string methods?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "How do you reverse a string?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is string slicing?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is list slicing?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is list comprehension?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is len() function?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is enumerate()?",
            },
            {"skill": "Python", "difficulty": "EASY", "question": "What is zip()?"},
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is the difference between append() and extend()?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is pop() in a list?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is sort() in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is the difference between sort() and sorted()?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is a lambda function?",
            },
            {"skill": "Python", "difficulty": "EASY", "question": "What is map()?"},
            {"skill": "Python", "difficulty": "EASY", "question": "What is filter()?"},
            {"skill": "Python", "difficulty": "EASY", "question": "What is reduce()?"},
            {"skill": "Python", "difficulty": "EASY", "question": "What is a package?"},
            {"skill": "Python", "difficulty": "EASY", "question": "What is pip?"},
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is Python's PEP 8?",
            },
            {
                "skill": "Python",
                "difficulty": "EASY",
                "question": "What is __name__ == '__main__'?",
            },
            # PYTHON MEDIUM (51-100)
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain *args and **kwargs in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are decorators in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "How do decorators work internally?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are generators in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the difference between generators and iterators?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is yield keyword in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain Python iterators.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are Python comprehensions?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain nested list comprehensions.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the difference between deep copy and shallow copy?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the copy module?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain mutable and immutable objects.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Why are tuples immutable?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is monkey patching in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is duck typing?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain polymorphism in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain inheritance in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is multiple inheritance?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is method resolution order (MRO)?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is super() in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain encapsulation in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain abstraction in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are abstract base classes?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the abc module?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are class methods?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are static methods?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are properties in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain property decorators.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are closures in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is lexical scoping?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain namespaces in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is LEGB rule in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain global and nonlocal keywords.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are context managers?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the with statement?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "How does file handling work in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are Python exceptions hierarchy?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "How do you create custom exceptions?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain regular expressions in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the re module?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "How do you read JSON files in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "How do you write JSON files in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is serialization in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the pickle module?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain Python virtual environments.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is the purpose of requirements.txt?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "Explain package management in Python.",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is threading in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What is multiprocessing in Python?",
            },
            {
                "skill": "Python",
                "difficulty": "MEDIUM",
                "question": "What are Python dataclasses?",
            },
            # JAVA EASY (1-25)
            {"skill": "Java", "difficulty": "EASY", "question": "What is Java?"},
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What are the main features of Java?",
            },
            {"skill": "Java", "difficulty": "EASY", "question": "What is JVM?"},
            {"skill": "Java", "difficulty": "EASY", "question": "What is JDK?"},
            {"skill": "Java", "difficulty": "EASY", "question": "What is JRE?"},
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is the difference between JDK, JRE, and JVM?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "Why is Java platform independent?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is a class in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is an object in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is the difference between a class and an object?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is a constructor in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is the default constructor?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What are instance variables?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What are local variables?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What are static variables?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is the static keyword?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is method overloading?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is method overriding?",
            },
            {"skill": "Java", "difficulty": "EASY", "question": "What is inheritance?"},
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is polymorphism?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is encapsulation?",
            },
            {"skill": "Java", "difficulty": "EASY", "question": "What is abstraction?"},
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What are access modifiers in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is the difference between == and equals()?",
            },
            {
                "skill": "Java",
                "difficulty": "EASY",
                "question": "What is the String class in Java?",
            },
            # JAVA MEDIUM (26-60)
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between String, StringBuilder, and StringBuffer?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "Why are Strings immutable in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the String Pool in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between Array and ArrayList?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the Java Collections Framework?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between List, Set, and Map?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between HashMap and Hashtable?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between HashMap and LinkedHashMap?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between HashMap and TreeMap?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "How does HashMap work internally?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is hashing in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is a hash collision and how is it handled?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are Generics in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are the advantages of Generics?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is type erasure in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is an interface in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between an abstract class and an interface?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are default methods in interfaces?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are functional interfaces?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are lambda expressions in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are method references in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is exception handling in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between checked and unchecked exceptions?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the purpose of finally block?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is try-with-resources?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is multithreading in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the difference between a process and a thread?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "How do you create a thread in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is synchronization in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the volatile keyword?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is serialization in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is the transient keyword?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are annotations in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What is reflection in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "MEDIUM",
                "question": "What are wrapper classes in Java?",
            },
            # JAVA HARD (61-100)
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain the internal working of the JVM.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are the different memory areas in JVM?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain Heap Memory and Stack Memory in Java.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How does Garbage Collection work in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are the different types of Garbage Collectors in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is the difference between Minor GC, Major GC, and Full GC?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain ClassLoader and its types.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How does Class Loading work in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is the Parent Delegation Model in ClassLoaders?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What happens internally when a Java program starts?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How does HashMap work internally in Java 8 and above?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How are collisions handled internally in HashMap?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain ConcurrentHashMap and its internal working.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is fail-fast and fail-safe iterator behavior?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How does TreeMap maintain sorted order internally?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain Red-Black Trees and their use in Java Collections.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is Thread Pooling and why is it used?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain the Executor Framework.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is ForkJoinPool in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain Callable and Future interfaces.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is CompletableFuture and how is it used?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are race conditions and how can they be prevented?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain deadlock with an example.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How can deadlocks be detected and avoided?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is the Java Memory Model (JMM)?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain happens-before relationship in Java.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are Atomic classes in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain Compare-And-Swap (CAS) operations.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is Reflection API and what are its drawbacks?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How do dynamic proxies work in Java?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are Java Streams and how do they work internally?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain parallel streams and their advantages and limitations.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are design patterns commonly used in Java applications?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "Explain Singleton Design Pattern and its thread-safe implementation.",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What is Dependency Injection and why is it important?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How does Spring IoC Container work internally?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are microservices and how are they implemented in Java ecosystems?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How would you optimize the performance of a large-scale Java application?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "How do you profile and troubleshoot memory leaks in Java applications?",
            },
            {
                "skill": "Java",
                "difficulty": "HARD",
                "question": "What are the trade-offs between Java, Python, and Go for backend systems?",
            },
            # SQL EASY (1-25)
            {"skill": "SQL", "difficulty": "EASY", "question": "What is SQL?"},
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What are the different types of SQL commands?",
            },
            {"skill": "SQL", "difficulty": "EASY", "question": "What is a database?"},
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is a table in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is a row and a column in a table?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is a Primary Key?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is a Foreign Key?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the difference between Primary Key and Foreign Key?",
            },
            {"skill": "SQL", "difficulty": "EASY", "question": "What is a Unique Key?"},
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the NOT NULL constraint?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the DEFAULT constraint?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the CHECK constraint?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the difference between DELETE, DROP, and TRUNCATE?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the SELECT statement?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "How do you filter records using WHERE clause?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the ORDER BY clause?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the GROUP BY clause?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the HAVING clause?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the DISTINCT keyword?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What are aggregate functions in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the COUNT() function?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What are the SUM(), AVG(), MIN(), and MAX() functions?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is a NULL value in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the LIKE operator?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the IN operator?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the BETWEEN operator?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the IS NULL operator?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is the difference between INNER JOIN and OUTER JOIN?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What are the different types of OUTER JOINs?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is a self join in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "EASY",
                "question": "What is a cross join in SQL?",
            },
            # SQL MEDIUM (26-60)
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is normalization in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are the different normal forms?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "Explain First Normal Form (1NF).",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "Explain Second Normal Form (2NF).",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "Explain Third Normal Form (3NF).",
            },
            {"skill": "SQL", "difficulty": "MEDIUM", "question": "What is BCNF?"},
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is denormalization and when would you use it?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are joins in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is an INNER JOIN?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is a LEFT JOIN?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is a RIGHT JOIN?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is a FULL OUTER JOIN?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is a SELF JOIN?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is a CROSS JOIN?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is the difference between WHERE and HAVING?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are subqueries in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is a correlated subquery?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is the EXISTS operator?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is the difference between EXISTS and IN?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are views in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are materialized views?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are indexes in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is the difference between clustered and non-clustered indexes?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "How do indexes improve query performance?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are composite indexes?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are transactions in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are ACID properties?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is COMMIT in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is ROLLBACK in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is SAVEPOINT in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is the difference between DELETE and TRUNCATE?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is a stored procedure?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are triggers in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What is the CASE statement in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "MEDIUM",
                "question": "What are Common Table Expressions (CTEs)?",
            },
            # SQL HARD (61-100)
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How does a database query optimizer work?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is an execution plan in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How do you analyze and optimize a slow SQL query?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is index selectivity and why is it important?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are covering indexes?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "When can indexes degrade performance?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is partitioning in databases?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is sharding and how does it differ from partitioning?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "Explain horizontal and vertical partitioning.",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is database denormalization and what trade-offs does it introduce?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are window functions in SQL?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "Explain ROW_NUMBER(), RANK(), and DENSE_RANK().",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is the difference between RANK() and DENSE_RANK()?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How do LEAD() and LAG() functions work?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are recursive Common Table Expressions (CTEs)?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How would you find duplicate records efficiently in a large table?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How would you delete duplicate rows while retaining one copy?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is database locking?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "Explain shared locks and exclusive locks.",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is a deadlock in SQL databases?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How can deadlocks be detected and resolved?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are transaction isolation levels?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "Explain Read Uncommitted, Read Committed, Repeatable Read, and Serializable isolation levels.",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are dirty reads, non-repeatable reads, and phantom reads?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How does MVCC (Multi-Version Concurrency Control) work?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is the CAP theorem and how does it relate to databases?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is eventual consistency?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How do replication strategies work in relational databases?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is the difference between master-slave and master-master replication?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How would you design a database schema for a large-scale e-commerce platform?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How would you optimize a database handling millions of transactions per day?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are materialized views and when should they be used?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How do triggers impact database performance?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are database migrations and why are they important?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How do you handle schema changes in production databases?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What are star schema and snowflake schema in data warehousing?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What is OLTP versus OLAP?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How would you troubleshoot a sudden database performance degradation?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "What metrics would you monitor for database health and performance?",
            },
            {
                "skill": "SQL",
                "difficulty": "HARD",
                "question": "How do modern relational databases handle concurrency at scale?",
            },  # REACT EASY (1-25)
            {"skill": "React", "difficulty": "EASY", "question": "What is React?"},
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What are the main features of React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "Why is React called a library and not a framework?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is a component in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What are functional components?",
            },
            {"skill": "React", "difficulty": "EASY", "question": "What is JSX?"},
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What are props in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is state in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is the difference between props and state?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is useState hook?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "How do you update state in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is useEffect hook?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is the Virtual DOM?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "How is Virtual DOM different from Real DOM?",
            },
            {"skill": "React", "difficulty": "EASY", "question": "What is ReactDOM?"},
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "Why are keys used in React lists?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is event handling in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "How do you conditionally render components in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What are forms in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is a controlled component?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is an uncontrolled component?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is React Fragment?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What is the purpose of React.StrictMode?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "What are inline styles in React?",
            },
            {
                "skill": "React",
                "difficulty": "EASY",
                "question": "How do you apply CSS in React applications?",
            },
            # REACT MEDIUM (26-60)
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "Explain the React component lifecycle.",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is reconciliation in React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How does the Virtual DOM improve performance?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is React Fiber?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are React Hooks?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are the rules of Hooks?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is useContext and when would you use it?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is useReducer and how is it different from useState?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is useRef and when should it be used?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is useMemo and why is it useful?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is useCallback and when should it be used?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is React.memo?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is prop drilling and how can it be avoided?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is Context API?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are Higher Order Components (HOCs)?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is render props pattern?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is code splitting in React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is lazy loading in React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How does React.lazy work?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is Suspense in React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is React Router?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How do you implement dynamic routing in React Router?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is nested routing in React Router?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are custom hooks in React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How do you handle API calls in React applications?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is Axios and why is it commonly used with React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How do you handle forms using React Hooks?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are controlled versus uncontrolled forms?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How do you manage global state in React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are the advantages of Redux over Context API?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What is Redux Toolkit?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How do you optimize React component rendering?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are React Portals?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "What are Error Boundaries in React?",
            },
            {
                "skill": "React",
                "difficulty": "MEDIUM",
                "question": "How do Error Boundaries improve application reliability?",
            },  # REACT HARD (61-100)
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "Explain React Fiber architecture in detail.",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How does React's reconciliation algorithm work internally?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How does React schedule updates?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What is Concurrent Rendering in React?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What problem does Concurrent Rendering solve?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What is React Server Components?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How do Server Components differ from Client Components?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What is hydration in React?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What are hydration mismatches and how can they be prevented?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "Explain Server-Side Rendering (SSR) in React.",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What are the advantages and disadvantages of SSR?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What is Static Site Generation (SSG)?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What is Incremental Static Regeneration (ISR)?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How does React.memo work internally?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "When can useMemo negatively impact performance?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "When should useCallback be avoided?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "Explain React rendering phases.",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What causes unnecessary re-renders in React applications?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How would you profile and optimize a slow React application?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What is code splitting and how is it implemented at scale?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How do Suspense and lazy loading work internally?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What are render waterfalls and how can they be avoided?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How does Context API affect rendering performance?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How would you design state management for a large React application?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "Compare Redux, Context API, Zustand, and Recoil.",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How does Redux Toolkit simplify Redux development?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What are middleware in Redux and how do they work?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What is React Query and what problems does it solve?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How do you implement caching in React applications?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How do you handle authentication and authorization in React?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How would you implement protected routes in React Router?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How do React Portals work internally?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How are Error Boundaries implemented in React?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What are custom renderers in React?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How does React Native differ from React internally?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How would you architect a scalable React application used by millions of users?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What are common React security vulnerabilities and how can they be mitigated?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How do micro-frontends work with React?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "How would you migrate a large legacy React application to modern React patterns?",
            },
            {
                "skill": "React",
                "difficulty": "HARD",
                "question": "What trade-offs should be considered when choosing React for large-scale systems?",
            },
            # JAVASCRIPT EASY (1-25)
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What are the main features of JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is the difference between JavaScript and Java?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "How do you declare variables in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is the difference between var, let, and const?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What are JavaScript data types?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What are primitive data types in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is a JavaScript object?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is an array in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is the difference between == and ===?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is type coercion in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What are functions in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is an arrow function?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is a callback function?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is the DOM?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "How do you select an element from the DOM?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is event handling in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is event bubbling?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is event capturing?",
            },
            {"skill": "JavaScript", "difficulty": "EASY", "question": "What is JSON?"},
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is localStorage?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is sessionStorage?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is the difference between null and undefined?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What are template literals?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "EASY",
                "question": "What is destructuring in JavaScript?",
            },  # JAVASCRIPT MEDIUM (26-60)
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is scope in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is the difference between global, function, and block scope?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is hoisting in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "How do let and const behave differently from var during hoisting?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is the Temporal Dead Zone (TDZ)?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are closures in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are practical use cases of closures?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is lexical scope in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is the this keyword in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "How does this behave in regular functions versus arrow functions?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are call(), apply(), and bind()?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is prototypal inheritance?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is the prototype chain?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is the difference between __proto__ and prototype?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are ES6 classes and how do they relate to prototypes?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are modules in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is the difference between CommonJS and ES Modules?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is asynchronous programming?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is the event loop in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are callbacks and callback hell?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are Promises in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are the states of a Promise?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is async/await?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is Promise.all()?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is Promise.race()?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is error handling in asynchronous code?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are higher-order functions?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are map(), filter(), and reduce()?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is currying in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is debouncing?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is throttling?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What is event delegation?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are Set and Map objects in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "What are WeakMap and WeakSet?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "MEDIUM",
                "question": "How do JavaScript modules improve application structure?",
            },  # JAVASCRIPT HARD (61-100)
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How does the JavaScript engine work internally?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are the parsing, compilation, and execution phases in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How does the V8 engine optimize JavaScript code?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What is Just-In-Time (JIT) compilation in JavaScript engines?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How does garbage collection work in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What causes memory leaks in JavaScript applications?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How would you identify and fix memory leaks in a web application?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "Explain the JavaScript event loop in detail.",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are microtasks and macrotasks?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What is the execution order of microtasks and macrotasks?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How do async/await work internally?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How are Promises implemented under the hood?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are generators in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How do generators differ from async functions?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are iterators and iterable protocols?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are Symbols and when should they be used?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How does prototypal inheritance work internally?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What is the difference between classical and prototypal inheritance?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How does the prototype chain resolve property lookups?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are property descriptors in JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are Proxy objects and how do they work?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What is the Reflect API?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How do closures affect memory management?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are currying and partial application, and how do they differ?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How would you implement debounce from scratch?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How would you implement throttle from scratch?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are Web Workers and when should they be used?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How does browser rendering interact with JavaScript execution?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What is the Critical Rendering Path?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How would you optimize the performance of a large JavaScript application?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are tree shaking and code splitting?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How do bundlers like Webpack, Vite, or Rollup work?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are source maps and why are they useful?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How do ES modules work internally in browsers?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What security risks are common in JavaScript applications?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How can Cross-Site Scripting (XSS) attacks be prevented?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How does Cross-Origin Resource Sharing (CORS) work?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How would you design a scalable front-end architecture using JavaScript?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "What are the trade-offs between JavaScript and TypeScript in large applications?",
            },
            {
                "skill": "JavaScript",
                "difficulty": "HARD",
                "question": "How do modern frameworks leverage JavaScript internals for performance?",
            },  # DBMS EASY (1-25)
            {"skill": "DBMS", "difficulty": "EASY", "question": "What is DBMS?"},
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What are the advantages of a DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is the difference between DBMS and a file system?",
            },
            {"skill": "DBMS", "difficulty": "EASY", "question": "What is a database?"},
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What are tables, rows, and columns?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is a schema in DBMS?",
            },
            {"skill": "DBMS", "difficulty": "EASY", "question": "What is metadata?"},
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is a DBMS instance?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What are the different types of databases?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is a relational database?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is a primary key?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is a foreign key?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is a candidate key?",
            },
            {"skill": "DBMS", "difficulty": "EASY", "question": "What is a super key?"},
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is normalization?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What are the different normal forms?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is data redundancy?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is data integrity?",
            },
            {"skill": "DBMS", "difficulty": "EASY", "question": "What is an ER model?"},
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What are entities and attributes?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is the difference between a weak entity and a strong entity?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is cardinality in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What are constraints in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What is referential integrity?",
            },
            {
                "skill": "DBMS",
                "difficulty": "EASY",
                "question": "What are ACID properties?",
            },  # DBMS MEDIUM (26-60)
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "Explain First Normal Form (1NF).",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "Explain Second Normal Form (2NF).",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "Explain Third Normal Form (3NF).",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is Boyce-Codd Normal Form (BCNF)?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is denormalization and when is it useful?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What are functional dependencies?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a partial dependency?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a transitive dependency?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is lossless decomposition?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is lossy decomposition?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a transaction in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What are transaction states in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is concurrency control?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is serializability in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is conflict serializability?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is view serializability?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is locking in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is Two-Phase Locking (2PL)?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a deadlock in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "How can deadlocks be prevented?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a database index?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "How do indexes improve performance?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a clustered index?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a non-clustered index?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is B-Tree indexing?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is hashing in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is a view in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What are materialized views?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is query processing in DBMS?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is query optimization?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What are joins and their types?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is the difference between inner join and outer join?",
            },
            {
                "skill": "DBMS",
                "difficulty": "MEDIUM",
                "question": "What is data warehousing?",
            },
            {"skill": "DBMS", "difficulty": "MEDIUM", "question": "What is OLTP?"},
            {"skill": "DBMS", "difficulty": "MEDIUM", "question": "What is OLAP?"},
            # DBMS HARD (61-100)
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Explain the internal architecture of a DBMS.",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are the different levels of database abstraction?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Explain physical, logical, and view levels of data abstraction.",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What is data independence and why is it important?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Explain the CAP theorem and its implications for databases.",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What is distributed database architecture?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are the challenges of distributed databases?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Explain horizontal and vertical fragmentation.",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What is database replication and why is it used?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are synchronous and asynchronous replication?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How does Multi-Version Concurrency Control (MVCC) work?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Explain optimistic versus pessimistic concurrency control.",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are dirty reads, non-repeatable reads, and phantom reads?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Explain transaction isolation levels in detail.",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How does Serializable isolation level work internally?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What is write-ahead logging (WAL)?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How does database recovery work after a system crash?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are checkpoints in database recovery?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Explain the ARIES recovery algorithm.",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How do B-Trees and B+ Trees differ?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "Why are B+ Trees preferred in database indexing?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How do hash indexes differ from tree-based indexes?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What is index selectivity and why is it important?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How does a query optimizer choose an execution plan?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are cost-based and rule-based query optimization techniques?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How would you optimize a slow-running query?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are database partitions and how do they improve scalability?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What is sharding and when should it be used?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are star schema and snowflake schema?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How do fact tables and dimension tables work in data warehouses?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What is a materialized view and how is it maintained?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How do NoSQL databases differ from relational databases?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "When would you choose a NoSQL database over a relational database?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are the trade-offs between consistency and availability?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How would you design a database for a social media platform?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How would you design a highly scalable e-commerce database?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What metrics should be monitored for database performance?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How would you troubleshoot database bottlenecks in production?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "What are common causes of database performance degradation?",
            },
            {
                "skill": "DBMS",
                "difficulty": "HARD",
                "question": "How do modern databases achieve high availability and fault tolerance?",
            },
            # OOP EASY (1-25)
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is Object-Oriented Programming (OOP)?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What are the four pillars of OOP?",
            },
            {"skill": "OOP", "difficulty": "EASY", "question": "What is a class?"},
            {"skill": "OOP", "difficulty": "EASY", "question": "What is an object?"},
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is the difference between a class and an object?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is encapsulation?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What are the benefits of encapsulation?",
            },
            {"skill": "OOP", "difficulty": "EASY", "question": "What is inheritance?"},
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What are the advantages of inheritance?",
            },
            {"skill": "OOP", "difficulty": "EASY", "question": "What is polymorphism?"},
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What are the different types of polymorphism?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is method overloading?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is method overriding?",
            },
            {"skill": "OOP", "difficulty": "EASY", "question": "What is abstraction?"},
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "Why is abstraction important?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is an abstract class?",
            },
            {"skill": "OOP", "difficulty": "EASY", "question": "What is an interface?"},
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is the difference between an abstract class and an interface?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What are constructors?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is a default constructor?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is constructor overloading?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is the this keyword?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is the super keyword?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What are access modifiers in OOP?",
            },
            {
                "skill": "OOP",
                "difficulty": "EASY",
                "question": "What is the difference between public, private, and protected access modifiers?",
            },
            # OOP MEDIUM (26-60)
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is the difference between aggregation and composition?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "Explain association in OOP.",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What are the different types of inheritance?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is multiple inheritance and what challenges does it introduce?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is hierarchical inheritance?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is multilevel inheritance?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "How does runtime polymorphism work?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "How does compile-time polymorphism work?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is dynamic binding?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is static binding?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is method hiding?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is object slicing?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is the difference between overloading and overriding?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is a virtual method?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is late binding in OOP?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is early binding in OOP?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "How does abstraction differ from encapsulation?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is information hiding?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What are static members in OOP?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What are nested classes?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is an immutable object?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "How do you design immutable classes?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What are object relationships in UML?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is a class diagram?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is a sequence diagram?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What are SOLID principles?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is the Single Responsibility Principle (SRP)?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is the Open/Closed Principle (OCP)?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is the Liskov Substitution Principle (LSP)?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is the Interface Segregation Principle (ISP)?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is the Dependency Inversion Principle (DIP)?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "How does dependency injection support OOP design?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is cohesion in software design?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "What is coupling in software design?",
            },
            {
                "skill": "OOP",
                "difficulty": "MEDIUM",
                "question": "Why is low coupling and high cohesion desirable?",
            },
            # OOP HARD (61-100)
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How is polymorphism implemented internally in object-oriented languages?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What are virtual tables (vtables) and how do they work?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How does dynamic dispatch work internally?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What are the trade-offs between inheritance and composition?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Why is composition often preferred over inheritance?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What problems can deep inheritance hierarchies cause?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How would you refactor a tightly coupled object-oriented system?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What is the diamond problem and how is it resolved in different languages?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How does multiple inheritance affect method resolution?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What is object composition in large-scale software architecture?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How do design patterns leverage OOP principles?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Factory Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Abstract Factory Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Builder Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Singleton Design Pattern and its limitations.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Prototype Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Adapter Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Decorator Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Facade Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Observer Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Strategy Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Command Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the State Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "Explain the Template Method Design Pattern.",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How do SOLID principles improve maintainability in large codebases?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How would you identify violations of SOLID principles in an existing project?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What is Dependency Injection and how does it support the Dependency Inversion Principle?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How does Inversion of Control (IoC) work?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What is the difference between Dependency Injection and Service Locator patterns?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How would you design a plugin-based architecture using OOP principles?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How do object-oriented systems handle scalability challenges?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What are common anti-patterns in object-oriented design?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What is the God Object anti-pattern?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What is the Anemic Domain Model anti-pattern?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How would you model a real-world e-commerce system using OOP concepts?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How would you design a library management system using OOP principles?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How would you design a ride-sharing application using object-oriented design?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "What are the trade-offs between object-oriented and functional programming paradigms?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "When might OOP be a poor fit for a software problem?",
            },
            {
                "skill": "OOP",
                "difficulty": "HARD",
                "question": "How do modern frameworks apply OOP principles under the hood?",
            },
            # DATA STRUCTURES EASY (1-25)
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a data structure?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "Why are data structures important?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is the difference between linear and non-linear data structures?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is an array?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What are the advantages and disadvantages of arrays?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a linked list?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is the difference between an array and a linked list?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a singly linked list?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a doubly linked list?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a circular linked list?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a stack?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What are the basic operations of a stack?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is LIFO?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a queue?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What are the basic operations of a queue?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is FIFO?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a circular queue?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a priority queue?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a deque?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a tree data structure?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a binary tree?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a binary search tree (BST)?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is a graph?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is the difference between a tree and a graph?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "EASY",
                "question": "What is hashing in data structures?",
            },
            # DATA STRUCTURES MEDIUM (26-60)
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How is memory allocated for arrays?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What are the time complexities of common array operations?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How do dynamic arrays work?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What are the advantages of linked lists over arrays?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How do insertion and deletion operations work in linked lists?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How would you detect a cycle in a linked list?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is Floyd’s Cycle Detection Algorithm?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How do stacks support recursion?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How would you implement a stack using queues?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How would you implement a queue using stacks?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What are the applications of priority queues?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is a heap data structure?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is the difference between a min heap and a max heap?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How are insertion and deletion performed in heaps?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is heapify operation?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What are tree traversals?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "Explain preorder, inorder, and postorder traversals.",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is level-order traversal?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How does a Binary Search Tree work?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What are the average and worst-case complexities of BST operations?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is a balanced binary tree?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is an AVL tree?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What are rotations in AVL trees?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is a Red-Black Tree?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What are the properties of a Red-Black Tree?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is graph traversal?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is Breadth-First Search (BFS)?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is Depth-First Search (DFS)?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is the difference between BFS and DFS?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How are graphs represented in memory?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is an adjacency matrix?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is an adjacency list?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is a hash table?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "How are collisions handled in hash tables?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "MEDIUM",
                "question": "What is separate chaining versus open addressing?",
            },
            # DATA STRUCTURES HARD (61-100)
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "Analyze the time and space complexity of common data structures.",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How would you choose the right data structure for a given problem?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are amortized time complexities and where are they used?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do dynamic arrays achieve amortized O(1) insertion?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a skip list and how does it work?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How does a trie data structure work?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are the applications of tries?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a suffix tree and when is it used?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a suffix array and how does it differ from a suffix tree?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do segment trees work?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are the applications of segment trees?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a Fenwick Tree (Binary Indexed Tree)?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How does a Fenwick Tree support range queries efficiently?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a B-Tree and where is it used?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a B+ Tree and why is it preferred in databases?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do AVL Trees maintain balance?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "Compare AVL Trees and Red-Black Trees.",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How does heap sort work internally?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is the union-find (disjoint set) data structure?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do path compression and union by rank optimize disjoint sets?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a sparse table and when is it useful?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How can Lowest Common Ancestor (LCA) queries be optimized?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are persistent data structures?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are immutable data structures and their advantages?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do bloom filters work?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are the trade-offs of using bloom filters?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How are graphs stored efficiently for large-scale systems?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is topological sorting and where is it used?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How would you detect cycles in a directed graph?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How would you detect cycles in an undirected graph?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What is a minimum spanning tree and why is it useful?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do Kruskal’s and Prim’s algorithms use data structures efficiently?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How does Dijkstra’s algorithm utilize priority queues?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are concurrent data structures?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do lock-free data structures work?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How would you design a scalable in-memory cache using data structures?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How is an LRU cache implemented efficiently?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "What are the trade-offs between arrays, linked lists, trees, and hash tables?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How would you optimize memory usage in large-scale data structure implementations?",
            },
            {
                "skill": "Data Structures",
                "difficulty": "HARD",
                "question": "How do modern databases and search engines leverage advanced data structures?",
            },
            # ALGORITHMS EASY (1-25)
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is an algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What are the characteristics of a good algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is time complexity?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is space complexity?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Big O notation?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Big Omega notation?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Big Theta notation?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is the time complexity of linear search?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is the time complexity of binary search?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What are the prerequisites for binary search?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is sorting?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Bubble Sort?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Selection Sort?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Insertion Sort?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Merge Sort?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is Quick Sort?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is recursion?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is the base case in recursion?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is divide and conquer?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is greedy strategy in algorithms?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is dynamic programming?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is backtracking?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is brute force approach?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is graph traversal?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "EASY",
                "question": "What is the difference between BFS and DFS?",
            },
            # ALGORITHMS MEDIUM (26-60)
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How do you analyze the time complexity of an algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How do you analyze the space complexity of an algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is amortized analysis?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "Compare Bubble Sort, Selection Sort, and Insertion Sort.",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does Merge Sort work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does Quick Sort work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is the worst-case scenario for Quick Sort?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does Heap Sort work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is Counting Sort and when is it useful?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is Radix Sort and when is it useful?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does Binary Search work internally?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How would you find the first or last occurrence of an element using Binary Search?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is recursion tree analysis?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How do you convert a recursive solution into an iterative one?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What are overlapping subproblems in Dynamic Programming?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is optimal substructure?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is memoization?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is tabulation in Dynamic Programming?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is the difference between memoization and tabulation?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What are common Dynamic Programming problem patterns?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does the greedy approach differ from Dynamic Programming?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is the activity selection problem?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is Huffman Coding?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does BFS work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does DFS work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How do you detect cycles in a graph using DFS?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is topological sorting?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is Kahn’s Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is Dijkstra’s Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What are the limitations of Dijkstra’s Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is Bellman-Ford Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What is Minimum Spanning Tree (MST)?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does Kruskal’s Algorithm work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "How does Prim’s Algorithm work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "MEDIUM",
                "question": "What are sliding window and two-pointer techniques?",
            },
            # ALGORITHMS HARD (61-100)
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "Explain Master Theorem and its applications.",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How do you solve recurrence relations using Master Theorem?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is asymptotic analysis and why is it important?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How would you compare two algorithms with different time and space complexities?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What are NP, NP-Complete, and NP-Hard problems?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How do NP-Complete problems differ from NP-Hard problems?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is the P versus NP problem?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is backtracking and how does it differ from brute force?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How does branch and bound work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is the N-Queens problem and how is it solved?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How would you solve the Subset Sum problem?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is the Knapsack problem and its variations?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How does Dynamic Programming optimize the Knapsack problem?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is Longest Common Subsequence (LCS) and how is it solved?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is Longest Increasing Subsequence (LIS)?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is Matrix Chain Multiplication?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is the Floyd-Warshall Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How does Bellman-Ford detect negative cycles?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is A* Search Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How do heuristic algorithms work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is bidirectional search?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How does Union-Find optimize graph algorithms?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is Tarjan’s Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is Kosaraju’s Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How do you find strongly connected components in a graph?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is network flow and where is it used?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is the Ford-Fulkerson Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is Edmonds-Karp Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How do segment trees support efficient range queries?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How do Fenwick Trees compare with Segment Trees?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What are suffix arrays and suffix trees?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How does the Rabin-Karp string matching algorithm work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What is the KMP (Knuth-Morris-Pratt) Algorithm?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How does Boyer-Moore string matching work?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What are randomized algorithms?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What are approximation algorithms and when are they used?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How would you design an algorithm for processing billions of records efficiently?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How do modern search engines leverage advanced algorithms?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "What are common algorithm optimization strategies used in large-scale systems?",
            },
            {
                "skill": "Algorithms",
                "difficulty": "HARD",
                "question": "How would you evaluate algorithmic trade-offs in real-world applications?",
            },
        ]
        created_count = 0

        for question in questions:

            _, created = QuestionBank.objects.get_or_create(
                skill=question["skill"],
                difficulty=question["difficulty"],
                question=question["question"],
                defaults={
                    "role": "",
                    "expected_answer": "",
                    "is_active": True,
                },
            )

            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"{created_count} new questions added successfully.")
        )
