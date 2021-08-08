/*
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
 */

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