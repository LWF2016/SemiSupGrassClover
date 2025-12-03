class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'irish':
            return '/kaggle/input/irish-grass-clover/camera'
        elif dataset == 'irish_ext':
            return '/kaggle/input/irish-grass-clover/camera'
        elif dataset == 'danish':
            return 'samples/danish'
        elif dataset == 'danish_ext':
            return 'samples/danish_ext'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
        
