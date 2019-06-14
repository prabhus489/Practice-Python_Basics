import os,time
import sys


def watching_dir():
    path_to_watch = "."
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while 1:
        time.sleep(10)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])

        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        for z in added:
            function_write(z)
            result = z
            print(result)
        before = after
        #if close == 1:
            #break


def function_write(file_name):
    # file_h = []
    main_zone_file = "../IS-nimble.zones"
    if os.path.isfile(main_zone_file):
        # print("*")
        with open(main_zone_file,'a') as mzone:
            mzone.write('''zone "%s" IN {\n\ttype master;\n\tfile "master/%s";\n\tallow-update { none; };\n};\n'''
                          %(file_name, file_name))
            mzone.flush()
            mzone.close()


watching_dir()
