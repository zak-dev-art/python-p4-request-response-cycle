# Flask Request-Response Cycle

## Running the Application

1. Navigate to the server directory:
   ```bash
   cd server
   ```

2. Set environment variables:
   ```bash
   source setup_env.sh
   ```
   Or manually:
   ```bash
   export FLASK_APP=app.py
   export FLASK_RUN_PORT=5555
   ```

3. Run the application:
   ```bash
   python app.py
   ```
   Or using Flask CLI:
   ```bash
   flask run
   ```

4. Visit `http://127.0.0.1:5555` in your browser

## Files

- `app.py` - Main Flask application with complete solution
- `examples.py` - Step-by-step examples from the lesson
- `setup_env.sh` - Environment variable setup script

## Testing Flask Shell

To test the URL map and other Flask features:

```bash
flask shell
```

Then in the shell:
```python
app.url_map
```