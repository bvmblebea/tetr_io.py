# tetr_io.py
Web-API for [tetr.io](https://tetr.io) website channel rest api 

## Example
```python3
import tetr_io
tetrachannel = tetr_io.TetraChannel()
latest_news = tetrachannel.get_latest_news()
print(f"-- Latest news::: {latest_news}")
```
