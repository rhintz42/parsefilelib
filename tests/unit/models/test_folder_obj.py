try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os

from outlib.lib.wout import output_to_file


class TestFolderObj(unittest.TestCase):
    def get_test_folder_path(self, folder_name):
        test_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
        return '%s/%s/' %(test_dir, folder_name)
 
    def test_init__folder_path(self):
        from parsefilelib.models.folder_obj import FolderObj

        test_folder_path = self.get_test_folder_path('test_files')
        folder_obj = FolderObj(test_folder_path)

        assert folder_obj.path == test_folder_path
 
    def test_init__folder_name(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        assert folder_obj.name == folder_name
 
    def test_init__files__test_files(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.files) >= 5
 
    def test_init__files__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.files) == 1
 
    def test_init__files__tests(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.files) == 1
 
    #################################################################
    def test_init__folders__test_files(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.folders) == 0
 
    def test_init__folders__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.folders) == 2
 
    def test_init__folders__tests__length(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.folders) == 3
 
    def test_init__folders__tests__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        for f in folder_obj.folders:
            if f.name == 'unit':
                unit_folder  = f
                break

        # TODO: Put in a better check
        assert unit_folder.name == 'unit'
        assert len(unit_folder.folders) == 2


    ################################################################
    def test_child_file_names__test_files(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_file_names) >= 5

    def test_child_file_names__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_file_names) == 1

    def test_child_file_names__tests(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_file_names) == 1


    ################################################################
    def test_child_folder_names__test_files(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folder_names) == 0

    def test_child_folder_names__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folder_names) == 2

    def test_child_folder_names__tests(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folder_names) == 3


    ################################################################
    def test_is_module__test_files(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.is_module == False

    def test_child_folder_names__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.is_module == True

    def test_child_folder_names__tests(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.is_module == True


    ################################################################
    def test_rec_child_files__test_files(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_files) >= 5

    def test_rec_child_files__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_files) >= 8

    def test_rec_child_files__tests(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_files) >= 14

    ################################################################
    def test_rec_child_folders__test_files(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_folders) == 0

    def test_rec_child_folders__unit(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_folders) == 2

    def test_rec_child_folders__tests(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_folders) == 5

    ################################################################
    def test_single_child_mode__simple(self):
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.single_child_mode == False

    def test_single_child_mode__file_obj_created_first(self):
        from parsefilelib.models.file_obj import FileObj
        from parsefilelib.models.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        test_file_path = "%s/%s" %(test_folder_path, 'simplest.py')
        file_obj = FileObj(test_file_path)
        folder_obj = FolderObj(test_folder_path, file_obj=file_obj)

        # TODO: Put in a better check
        assert folder_obj.single_child_mode == True


    ##########################################################################
    ######################## SURVEYMONKEY TEST FILES #########################
    ##########################################################################
    def test_rec_child_folders__anweb(self):
        """
        These tests will fail unless the specific file is on your computer
            in the specific place indicated by `test_file_path`
        NOTE: This file is NOT static, thus this test is bound to fail over
            time. IF it fails, then check to make sure there isn't a bug in
            this project.
            * If there is a bug, then fix it and make this test
                passing.
            * If there is no bug, then just make this test pass again
        """
        from parsefilelib.models.file_obj import FileObj
        from parsefilelib.models.folder_obj import FolderObj

        test_folder_path = '/opt/webapp/anweb/src/anweb/anweb/'
        folder_obj = FolderObj(test_folder_path)

        assert folder_obj.name == 'anweb'
        assert len(folder_obj.folders) == 5

        assert len(folder_obj.files) == 2

        test_file_path = '/opt/webapp/anweb/src/anweb/anweb/models/surveys.py'
        file_obj = FileObj(file_path=test_file_path)
        #output_to_file('/opt/webapp/proflib_visualizer/src/proflib_visualizer/proflib_visualizer/static/json/parse_file_lib_json_files/test_2.json',
        #                [folder_obj.to_dict()],
        #                append=False)

        """
        surveys_file_obj = folder_obj.folders[3].files[4]
        assert surveys_file_obj.name == 'surveys.py'

        assert len(surveys_file_obj.functions) == 0
        assert len(surveys_file_obj.classes) == 4
        # file_obj.classes[2] should be the Survey class
        assert len(surveys_file_obj.classes[2].functions) == 87
        # file_obj.classes[3] should be the Page class
        assert len(surveys_file_obj.classes[3].functions) == 9
        """
