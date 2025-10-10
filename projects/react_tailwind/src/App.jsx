import './App.css'

function App() {
    return (
        <>
            <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900">
                <div className="container mx-auto px-4 py-16">
                    <div className="text-center">
                        <h1 className="text-6xl font-bold text-white mb-4">
                            PsychoNoir-Kontrapunkt
                        </h1>
                        <p className="text-xl text-gray-300 mb-8">
                            Isolated Development Environment
                        </p>
                        <div className="bg-white/10 backdrop-blur-sm rounded-lg p-8 max-w-2xl mx-auto">
                            <h2 className="text-2xl font-semibold text-white mb-4">
                                React + TailwindCSS + Vite
                            </h2>
                            <p className="text-gray-300 mb-6">
                                This is a sample project demonstrating the PsychoNoir-Kontrapunkt
                                isolated development environment with modern web technologies.
                            </p>
                            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                                <div className="bg-white/20 rounded p-3">
                                    <div className="text-white font-semibold">Bun</div>
                                    <div className="text-gray-400">Runtime</div>
                                </div>
                                <div className="bg-white/20 rounded p-3">
                                    <div className="text-white font-semibold">Biome</div>
                                    <div className="text-gray-400">Linter</div>
                                </div>
                                <div className="bg-white/20 rounded p-3">
                                    <div className="text-white font-semibold">uv</div>
                                    <div className="text-gray-400">Python</div>
                                </div>
                                <div className="bg-white/20 rounded p-3">
                                    <div className="text-white font-semibold">Rust</div>
                                    <div className="text-gray-400">Systems</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default App