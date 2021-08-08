document.querySelectorAll('button[data-id]').forEach(
    (btn) => {
        btn.addEventListener(
            'click', async (e) => {
                btn.parentElement.remove()
                await fetch(`/delete/${btn.getAttribute('data-id')}`)
            }
        )
    }
)