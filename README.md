## Post writer



This post writer provides high-quality content with relevant tags.


## Prerequisites

  

1.  **Install Python**:

- Download Python from [Microsoft Store](https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare) or from the [official Python website](https://www.python.org/downloads/).

2.  **Add Python to System Path**:

- Ensure Python is added to your system path. By default, Python is usually located at:

```

C:\Users\[Your Username]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

```

- To add Python to your path:

- Open **Environment Variables** > **System Variables** > **Path** > **Edit**.

- Add the path to your Python directory containing `ipython.exe` (usually in the folder listed above).

- Click **OK** to save.



3. **Create groq api key**:

-  Create your groq api key from [Groq api key](https://console.groq.com/keys)

-  Add this key into .env file.



## Running the disease identifier

  

1.  **Install Dependencies**:

- Open Command Prompt in the folder where you saved the files.

- Run:

```bash

pip install -r requirements.txt

```



2. **Add neccesary details**:

- Add your name and email id in pyproject.toml file

- Create an .env file and add:

 ```bash

MODEL=groq/llama-3.3-70b-versatile
GROQ_API_KEY=your groq api key here

```

  

3.  **Run `post writer`**:

- Open terminal in your IDE.

- Run:

```bash

cd post_writer

```

```bash

crewai run

```
