const todosContainer: HTMLElement | null = document.getElementById("todos-container");
const addTodoForm: HTMLFormElement | null = document.getElementById("add-todo-form") as HTMLFormElement | null;

interface Todo {
    id: number;
    title: string;
    content: string;
    created_at: string;
}

const renderTodo = (todo: Todo) => {
    const todoElem = document.createElement("div");
    todoElem.setAttribute('data-id', String(todo.id));
    todoElem.innerHTML = `
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-xl font-semibold text-gray-700 dark:text-gray-200 max-w-sm truncate">${todo.title}</h2>
            <p class="text-sm text-gray-400 dark:text-gray-500">${todo.created_at}</p>
        </div>
        <div class="flex justify-between items-end">
            <p class="text-gray-500 dark:text-gray-400 whitespace-pre-wrap max-w-md">${todo.content}</p>
            <button class="delete-btn text-red-500 hover:text-red-700 focus:outline-none">
                Delete
            </button>
        </div>
    `;
    const deleteBtn = todoElem.querySelector(".delete-btn");
    if (deleteBtn) deleteBtn.addEventListener("click", () => deleteTodo(todo.id));
    return todoElem;
}

const fetchAndRenderTodos = async () => {
    const response = await fetch("/api/todos");
    const todos = await response.json();
    todos.forEach((todo: Todo) => {
        todosContainer?.appendChild(renderTodo(todo));
    });
}

const deleteTodo = async (id: number) => {
    const response = await fetch(`/api/todos/${id}`, {
        method: "DELETE"
    });
    if (response.ok) {
        const todoElem = todosContainer?.querySelector(`[data-id="${id}"]`);
        todoElem?.remove();
    } else alert("Failed to delete the todo item.")
}

addTodoForm?.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(addTodoForm);
    const data = Object.fromEntries(formData);

    const response = await fetch('/api/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        const newTodo = await response.json();
        todosContainer?.appendChild(renderTodo(newTodo));
        addTodoForm.reset();
    } else {
        alert('添加失败');
    }
});

document.addEventListener("DOMContentLoaded", fetchAndRenderTodos)