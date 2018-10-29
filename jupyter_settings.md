# How to change the Jupyter start-up folder?

If you're using a Windows System, you might encouter difficulties in setting the default path for Jupyter Notebook. Current information available online is pretty scattered. Below there is a working solution tested by me. 

1.  Add it to the global config file

    1.  Open "Anaconda Prompt" and type `jupyter notebook --generate-config`

    1.  Find the file in `C:\Users\username\.jupyter\jupyter_notebook_config.py`

    1.  Change the line of `#c.NotebookApp.notebook_dir = ''` to `c.NotebookApp.notebook_dir = 'c:\yourworkbench\'`

        1.  Remeber to remove the comment hashbang `#`

1.  Then, change the shortcut of Jupyter Notebook

    1.  go to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)`, right-mouse-click the "Jupyter Notebook" shortcut icon and open "Properties" dialog

    1.  In the Target field, remove `%USERPROFILE%`

    1.  In the field of "Start in", type the same directory of `c:\yourworkbench\` as abovementioned.

1.  Done!
