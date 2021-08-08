window.onload = () => {
    const forms = document.querySelectorAll('.delete-form')

    forms.forEach(
        (form, index) => {
            form.addEventListener(
                'submit', async (e) => {
                    e.preventDefault()
                    form.parentElement.remove()

                    await fetch(`/delete/${index}`)
                }
            )
        }
    )
}