class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = {}

        for course, pre in prerequisites:
            if pre in course_graph:
                course_graph[pre].append(course)
            else:
                course_graph[pre] = [course]
            
        visited = set()

        for current_course in range(numCourses):
            if not self.courseSchedule(current_course, visited, course_graph):
                return False
        
        return True

    def courseSchedule(self, course, visited, course_graph):
        if course in visited:
            return False
        
        if course_graph.get(course) is None:
            return True
        
        visited.add(course)

        for next_course in course_graph[course]:
            if not self.courseSchedule(next_course, visited, course_graph):
                return False

        visited.remove(course)

        course_graph[course] = None

        return True