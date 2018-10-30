It's tricky!

1.  Download Anaconda from TUNA's mirror 
    1.  Goto https://mirrors.tuna.tsinghua.edu.cn/
    1.  Click the “获取下载链接” button
    1.  Click “应用软件” -> “Conda”, pick up the version that corresponds to your OS.
        1.  As of writing this snippet, the latest version is 5.3, so I picked up https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.0-Windows-x86_64.exe        
    1.  Download and install it!

1.  Install Pytorch

    1.  Start menu, type in “anacon”,  Right mouse click “Anaconda Prompt” -> “Run as Administrator”，

    1.  Run the following commands
        ```
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
        conda config --set show_channel_urls yes

        conda install pytorch

        pip install torchvision
        ```

    
