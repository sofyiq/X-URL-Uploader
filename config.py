if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from sample_config import Config
  
