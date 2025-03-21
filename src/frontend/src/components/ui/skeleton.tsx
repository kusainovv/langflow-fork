import { cn } from "../../utils/utils";

function Skeleton({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn("animate-pulse   bg-border", className)}
      {...props}
    />
  );
}

export { Skeleton };
