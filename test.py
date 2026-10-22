
import marimo

__generated_with = "0.19.0"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    enabled = mo.ui.switch(label="Enable feature", value=False)
    enabled
    return (enabled,)


@app.cell
def _(enabled, mo):
    if enabled.value:
        mo.md("✅ **Feature is ON**")
    else:
        mo.md("⭕ **Feature is OFF**")
    return


if __name__ == "__main__":
    app.run()
