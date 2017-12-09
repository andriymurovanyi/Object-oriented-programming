# A software academy teaches two types of courses: local courses that are held in
# some of the academy’s local labs and offsite courses held in some other town outside of
# the academy’s headquarters. Each course has a name, a teacher assigned to teach it and a
# course program (sequence of topics). Each teacher has a name and knows the courses he
# or she teaches. Both courses and teachers could be printed in human-readable text form.
# All your courses should implement ICourse. Teachers should implement ITeacher. Local
# and offsite courses should implement ILocalCourse and IOffsiteCourse respectively.
# Courses and teachers should be created only through the ICourseFactory interface
# implemented by a class named CourseFactory.
# Write a program that will form courses of software academy.

from abstraction import *


class Course(ICourse):
    """
    This class used to implement ICourse.
    """

    def __init__(self, teacher, course_type, course_name, location):
        """
        Used to initialize parameters.
        
        :param teacher: teacher object
        :param course_type: type of course
        :param course_name: name of course
        :param location: where course is situated
        """

        self._themes = []
        self.extra_teachers = []
        if type(course_name) is str and type(course_type) is str \
                and type(location) is str and isinstance(teacher, Teacher):
            self._course_name = course_name
            self.course_type = course_type
            self.location = location
            self.teacher = teacher
        else:
            raise TypeError

    @property
    def course_name(self):
        """
        Getter for course name
        :return: course name
        """
        return self._course_name

    def __str__(self):
        """
        Printable form.
        
        Used to print information about course in comfortable readable form.
        :return: information about course
        """
        return 'Teachers: ' + str([self.teacher.teacher_name]) + ' ' + \
               str([i.teacher_name for i in self.extra_teachers]) \
               + '\n' + \
               'Course name: ' + str(self._course_name) + '\n' + \
               'Course type: ' + str(self.course_type) + '\n' + \
               'Themes: ' + str(self._themes) + '\n' + \
               'Location: ' + str(self.location)

    def addTheme(self, new_theme):
        """
        Used to add new theme to course.
        """
        self.themes.append(new_theme)

    def addTeacherToCourse(self, teacher):
        """
        Adding new teacher to course.
        :param teacher: one more teacher in course.
        """
        self.extra_teachers.append(teacher)

    @property
    def themes(self):
        """
        Getter for all themes in course.
        :return: all themes.
        """
        return self._themes


class Teacher(ITeacher):
    """
    Used to implement ITeacher.
    """

    def __init__(self, teacher_name):
        """
        Used to initialize parameters.
        :param teacher_name: name of teacher of the course
        """
        self._teacher_name = teacher_name
        self._courses = []  # All courses for current teacher.

    @property
    def teacher_name(self):
        """
        Used to print teacher name.
        :return: teacher name
        """
        return self._teacher_name

    def __str__(self):
        """
        Printable form.

        Used to print information about teacher in comfortable readable form.
        :return: information about teacher
        """
        return 'Teacher name: ' + str(self.teacher_name) + '\n' + \
               'Courses: ' + str([i._course_name for i in self._courses])

    @property
    def courses(self):
        """
        Used to print all courses for current teacher.
        :return: all courses
        """
        return self._courses

    def addTeacherCourse(self, course):
        """
        New course.
        
        Adding one more course to teacher.
        :param course: new course.
        """
        self.courses.append(course)


class LocalCourse(ILocalCourse, Course):
    """
    Used to implement ILocalCourse.
    """
    course_type = 'Local course'
    location = 'Lecture hall'

    def __init__(self, course_name, teacher):
        super().__init__(course_name, self.course_type, teacher, self.location)


class OffsiteCourse(IOffsiteCourse, Course):
    """
    Used to implement IOffsiteCourse.
    """
    course_type = 'Offsite course'
    location = 'City'

    def __init__(self, course_name, teacher):
        super().__init__(course_name, self.course_type, teacher, self.location)


class CourseFactory(ICourseFactory):
    """
    Creating.
    
    Used to create new teachers and courses
    """

    @staticmethod
    def create_teacher(teacher_name):
        """
        Teacher.
        
        Create Teacher object.
        :param teacher_name: name of teacher
        :return: instance of Teacher.
        """
        return Teacher(teacher_name)

    @staticmethod
    def create_local_course(teacher, course_name):
        """
        Local Course.
        
        Create LocalCourse object
        ::param teacher: instance of Teacher
        ::param course_name: name for new local course
        """
        return LocalCourse(teacher, course_name)

    @staticmethod
    def create_offsite_course(teacher, course_name):
        """
        Offsite Course.

        Create Offsite Course object
        ::param teacher: instance of Teacher
        ::param course_name: name for new offsite course
        """
        return OffsiteCourse(teacher, course_name)


t = CourseFactory.create_teacher('Tymchuk Oleg Sergeevich')
t2 = CourseFactory.create_teacher('Ukrainets Irina Vladimirovna')
t3 = CourseFactory.create_teacher('Paramonov Anton Ivanovich')
c = CourseFactory.create_local_course(t, 'Introduction to OOP')
c.addTeacherToCourse(t2)
t.addTeacherCourse(c)
c.addTheme('Encapsulation')
c.addTheme('Inheritance')
c.addTheme('Polymorphism')
print(c)
print('===========================================')
c2 = CourseFactory.create_offsite_course(t, 'GUI')
c2.addTeacherToCourse(t3)
c2.addTheme('Introduction')
c2.addTheme('Widgets')
t.addTeacherCourse(c2)
print(c2)
print('===========================================')
print(t)
