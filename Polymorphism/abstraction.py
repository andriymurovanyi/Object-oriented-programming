# Abstract Base Classes.
from abc import ABCMeta, abstractmethod, abstractstaticmethod


class ICourse(metaclass=ABCMeta):
    """
    Should be implemented by Courses.
    """

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def course_name(self):
        pass

    @abstractmethod
    def addTheme(self):
        pass

    @property
    @abstractmethod
    def themes(self):
        pass

    @abstractmethod
    def addTeacherToCourse(self):
        pass


class ITeacher(metaclass=ABCMeta):
    """
    Should be implemented by Teachers.
    """
    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def teacher_name(self):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass

    @abstractmethod
    def addTeacherCourse(self):
        pass


class ILocalCourse(ICourse):
    """
    Should be implemented by LocalCourses.
    """
    pass


class IOffsiteCourse(ICourse):
    """
    Should be implemented by OffsiteCourses.
    """
    pass


class ICourseFactory(metaclass=ABCMeta):
    """
    Should be implemented by CourseFactory.
    """

    @abstractstaticmethod
    def create_teacher(self):
        pass

    @abstractstaticmethod
    def create_local_course(self):
        pass

    @abstractstaticmethod
    def create_offsite_course(self):
        pass


