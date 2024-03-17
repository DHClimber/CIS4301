import { Button } from "@mui/material";
import { useRouter } from "next/navigation";

export function BackButton() {
    const router = useRouter();
    return(
        <Button variant="contained" onClick={() => router.back()}>Back</Button>
    )
}