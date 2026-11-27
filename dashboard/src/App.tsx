import { Button } from '@/components/ui/button'

function App() {
  return (
    <main className="flex min-h-svh flex-col items-center justify-center gap-4 p-6">
      <h1 className="text-2xl font-semibold">Support Dashboard</h1>
      <p className="text-muted-foreground">Nothing here yet.</p>
      <Button variant="outline" asChild>
        <a href="/health">API health</a>
      </Button>
    </main>
  )
}

export default App
