$val1=0
$val2=0
function suma
{
    param([Parameter(Mandatory)][int]$num1,[Parameter(Mandatory)][int]$num2)
    Write-Host "La suma es" ($num1 + $num2)
}
$respuesta= Read-Host "¿Quiere realizar una suma? 0=no, 1=si"
if($respuesta -eq 1)
{
    do
    {
        $val1=Read-Host -Prompt "Ingrese el primer numero:"
        $val2= Read-Host -Prompt "Ingrese el segundo numero:"
        suma -num1 $val1 -num2 $val2
        $respuesta= Read-Host -Prompt "¿Quiere volver a hacer una suma? 0=no, 1=si"
    }while($respuesta -eq 1)
}
Write-Host "Gracias por utilizar este programa"