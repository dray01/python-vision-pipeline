

def test_blah(rewriter, capsys):
    sample = rewriter("dlp_inspect_image_file.py",
        [
            "project_id": "...",
            "file_path": "..."
        ])
    sample.run()

    out, _  = capsys.readouterr()
