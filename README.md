
---
<div align="center">
  <h1>IITP student interpolation project</h1>
</div>

### project paper

https://www.overleaf.com/project/675a076aed19c14b501fd5e3

### project installation && setup: 🚀

1) ```git clone https://github.com/kirbu123/iitp_interpolation.git```

2) ```cd iitp_interpolation```

### poetry setup: 🔥

1) ```curl -sSL https://install.python-poetry.org | python3 - && poetry --version```

2) ```poetry config virtualenvs.in-project true```

3) ```cd iitp_interpolation```

4) ```poetry install```

### ruff check && fix: ✅

1) ```poetry run ruff check --fix```

    ### it have to show: ``` All checks passed! ```

### run project: 👍

1) ### cartesiangrid: 
    ```poetry run cartesiangrid --image_path [...]  --limits [...] --points [...]```

2) ### interp
    ```poetry run interp```

3) ### regulargrid
    ```poetry run regulargrid```