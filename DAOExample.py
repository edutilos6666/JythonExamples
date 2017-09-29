from java.lang import String
from java.util import HashMap, ArrayList

class Worker:
    def __init__(self, id = 0, name = "", age = 0, wage =0.0, active = False):
        self.id = id
        self.name = name
        self.age = age
        self.wage = wage
        self.active = active


    def __repr__(self):
        return String.format("Worker(%d, %s, %d, %.2f, %s)",
                             self.id, self.name, self.age, self.wage, self.active)



class WorkerDAO:
    def save(self, worker):
        pass

    def update(self, id, newWorker):
        pass

    def remove(self, id):
        pass

    def find_by_id(self, id):
        pass

    def find_all(self):
        pass


class WorkerDAOImpl(WorkerDAO):
    def __init__(self):
        self.container =  HashMap()

    def save(self, worker):
        self.container.put(worker.id , worker)

    def update(self, id, newWorker):
        self.container.remove(id)
        self.container.put(id, newWorker)

    def remove(self, id):
        self.container.remove(id)

    def find_by_id(self, id):
        return self.container.get(id)

    def find_all(self):
        return self.container.values()



class DAOExample:
    def example1(self):
        workerList = ArrayList()
        workerList.add(Worker(1, "foo", 10, 100.0, True))
        workerList.add(Worker(2, "bar", 20, 200.0, False))
        workerList.add(Worker(3, "bim", 30, 300.0, True))

        dao = WorkerDAOImpl()
        for w in workerList:
            dao.save(w)

        all = dao.find_all()
        print("<<all workers>>")
        for w in all:
            print(w)

        # update
        dao.update(1, Worker(1, "new foo", 66, 666.6, False))
        one = dao.find_by_id(1)
        print("one after update = {0}".format(one))

        # remove
        dao.remove(1)
        all = dao.find_all()
        print("<<all workers after remove>>")
        for w in all:
            print(w)



